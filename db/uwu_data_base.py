import sqlalchemy as db
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, Text
import csv
import json
import requests
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///db/uwu.db', echo=False)
Session = sessionmaker(bind=engine)
conn = Session()
import sqlalchemy.orm
Base = sqlalchemy.orm.declarative_base()
metadata = db.MetaData()
csv.field_size_limit(200000)

PNVHS_add_edu_sphere = {
    'Академия транспортных технологий': 'Промышленный сектор',
    'Государственный университет морского и речного флота имени адмирала С.О. Макарова': 'Повышение квалификации',
    'Академия управления городской средой, градостроительства и печати': 'IT',
}

class Priem(Base):
    __tablename__ = 'priem'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    ege1 = Column(String)
    ege2 = Column(String)
    ege3 = Column(String)
    min1 = Column(Integer)
    min2 = Column(Integer)
    min3 = Column(Integer)
    last_year = Column(Integer)

class Special(Base):
   __tablename__ = 'special'
   
   id = Column(Integer, primary_key = True)
   plan_id = Column(Integer)
   name = Column(String)
   specialty_id = Column(Integer)
   department_id = Column(Integer)
   fakultet_id = Column(Integer)
   study_period = Column(Integer)
   study_form_id = Column(Integer)
   study_level_id = Column(Integer)

class Vacancy(Base):
    __tablename__ = 'vacancy'

    id = Column(Integer, primary_key=True)
    sphere = Column(Text)
    skills = Column(Text)


class EtuStrPlan(Base):
    __tablename__ = 'etu_str_plan'

    id = Column(Integer, primary_key=True)
    etu_id = Column(Integer)
    subject = Column(Text)
    hours = Column(Integer)
    plan_id = Column(Integer)
    type = Column(Text)

class EtuSubject(Base):
    __tablename__ = 'etu_subject'

    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer)
    plan_str_id = Column(Integer)
    ze = Column(Integer)
    hours = Column(Integer)
    sem = Column(Integer)
    exam = Column(db.Boolean)
    offset = Column(db.Boolean)
    diff_offset = Column(db.Boolean)
    course_work = Column(db.Boolean)

class Summary(Base):
    __tablename__ = 'summary'
    id = Column(Integer, primary_key=True)
    summary = Column(Text)
    subject = Column(Text)

class AddEdu(Base):
    __tablename__ = 'add_edu'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    site = Column(Text)
    org_name = Column(Text)
    org_address = Column(Text)
    logo_url = Column(Text)
    type = Column(Text)
    edu_form = Column(Text)
    phone = Column(Text)
    email = Column(Text)
    starts = Column(Text)
    cost = Column(Integer)
    edu_len = Column(Integer)

def getSpecialties(fakultet_id: int, session):
    select_all_query = session.query(Special).filter(Special.fakultet_id == fakultet_id).all()
    return select_all_query

def get_awesome_proff_sphere(plan_id: int, session):
    d = {}
    subjects = conn.query(EtuStrPlan).filter(EtuStrPlan.plan_id == plan_id).all()
    for subj in subjects:
        a = conn.query(EtuSubject).filter(EtuSubject.plan_str_id == subj.etu_id).all()
        for inf_subj in a:
            if subj.subject not in d:
                d[subj.subject] = 0
            d[subj.subject] += inf_subj.ze
    d_sphere = {}
    spheres = []
    for sphere in session.query(Vacancy).all():
        if sphere.sphere != '' and sphere.sphere:
            d_sphere[sphere.sphere] = sphere.skills.split(',')
    for sphere in d_sphere:
        score = 0
        for skill in d_sphere[sphere]:
            if skill in d: score += d[skill]
        spheres.append([sphere, score])
    spheres.sort(key=lambda x: x[1], reverse=True)
    print(spheres)

def addPriem(conn, engine, filename):
    r = []
    i = 0
    ids = set()
    with open(filename) as f:
        s = f.read()
        l = json.loads(s)
        for x in l:
            i += 1
            maybe_id = conn.query(Special.id).filter(Special.name == x["Направление"]).all()[0][0]
            if maybe_id in ids:
                continue
            p = Priem(
                id   = maybe_id,
                name = x["Направление"],
                ege1 = x["Предмет 1"],
                ege2 = x["Предмет 2"],
                ege3 = x["Предмет 3"],
                min1 = x["Мин. балл 1"],
                min2 = x["Мин. балл 2"],
                min3 = x["Мин. балл 3"],
                last_year = x["Балл"]
            )
            r.append(p)
            ids.add(maybe_id)
    print(i)
    return r


def get_edu_prog(plan_id: int, custom_conn):
    facs = {30: 'ГФ', 42: 'ИНПРОТЕХ', 24: 'ФРТ', 25: 'ФЭЛ', 26: 'ФКТИ', 27: 'ФЭА', 28: 'ФИБС'}
    study_form = {
    1: "Специалитет",
    2: "Бакалавриат",
    3: "Магистратура",
    7: "Аспирантура"}
    departments = {1: ['Автоматики и процессов управления', 'АПУ'], 2: ['"Информационные системы"', 'ИС'], 3: ['Биотехнических систем', 'БТС'], 4: ['Высшей математики', 'ВМ'], 5: ['"Алгоритмическая математика"', 'АМ'], 6: ['Вычислительной техники', 'ВТ'], 7: ['Инженерной защиты окружающей среды', 'ИЗОС'], 8: ['Инновационного менеджмента', 'ИМ'], 9: ['Иностранных языков', 'ИНЯЗ'], 10: ['Информационно-измерительных систем и технологий', 'ИИСТ'], 11: ['Фотоники', 'Фот'], 12: ['Корабельных систем управления', 'КСУ'], 13: ['Лазерных измерительных и навигационных систем', 'ЛИНС'], 14: ['Математического обеспечения и применения ЭВМ', 'МОЭВМ'], 15: ['Менеджмента и систем качества', 'МСК'], 16: ['Микрорадиоэлектроники и технологии радиоаппаратуры', 'МИТ'], 17: ['Микро- и наноэлектроники', 'МНЭ'], 18: ['Прикладной механики и инженерной графики', 'ПМИГ'], 19: ['Прикладной экономики', 'ПЭ'], 20: ['Радиотехнических систем', 'РС'], 21: ['Микроволновой электроники', 'МВЭ'], 22: ['Радиоэлектронных средств', 'РЭС'], 23: ['Робототехники и автоматизации производственных систем', 'РАПС'], 24: ['Систем автоматизированного проектирования', 'САПР'], 25: ['Систем автоматического управления', 'САУ'], 26: ['"Связи с общественностью"', 'СО'], 27: ['Телевидения и видеотехники', 'ТВ'], 28: ['Теоретических основ радиотехники', 'ТОР'], 29: ['Теоретических основ электротехники', 'ТОЭ'], 30: ['Физики', 'Физики'], 31: ['Физической химии', 'ФХ'], 32: ['Физической электроники и технологии', 'ФЭТ'], 33: ['Физического воспитания и спорта', 'ФВиС'], 34: ['Электроакустики и ультразвуковой техники', 'ЭУТ'], 35: ['Электронного приборостроения', 'ЭП'], 36: ['Электронных приборов и устройств', 'ЭПУ'], 37: ['Электротехнологической и преобразовательной техники', 'ЭТПТ'], 39: ['Безопасности жизнедеятельности', 'БЖД'], 40: ['Истории культуры, государства и права', 'ИКГП'], 41: ['Русского языка', 'РЯ'], 42: ['Социологии и политологии', 'СП'], 43: ['Философии', 'ФЛ'], 44: ['Экономики технологического предпринимательства', 'ЭТП'], 45: ['Базовая кафедра автоматизации исследований', 'Баз.АИ'], 46: ['Базовая кафедра "Интеллектуальные информационные технологии"', 'Баз.ИИТ'], 47: ['Медицинских технологий (базовая)', 'Баз.МТ'], 48: ['Базовая кафедра оптоэлектроники', 'Баз.ОЭ'], 49: ['Базовая кафедра радиоастрономии', 'Баз.РА'], 50: ['Базовая кафедра радиоэлектронных информационных систем и комплексов', 'Баз.РИСК'], 51: ['Базовая кафедра специальных средств радиоэлектроники', 'Баз.ССР'], 52: ['Базовая кафедра конструирования и производства судового электрооборудования', 'БККИПСЭ'], 53: ['Базовая кафедра технологии производства радиодеталей', 'БКТПР'], 54: ['Базовая кафедра конструирования и технологии электронной аппаратуры', 'Баз.КТЭА'], 55: ['Физики и современной технологии твердотельной электроники', 'Баз.ФТТЭ'], 58: ['Информационная безопасность', 'ИБ'], 59: ['Базовая кафедра "Вычислительные технологии"', 'Баз.ВТ'], 60: ['Базовая кафедра "Наноматериалы и нанотехнологии в радиоэлектронике"', 'Баз.ННР'], 61: ['Базовая кафедра "Медицинские информационные и биотехнические системы"', 'Баз.МИБТС'], 62: ['Базовая кафедра "Видеоинформационные системы"', 'Баз.ВИНС'], 63: ['Базовая кафедра "Программное и аппаратное обеспечение гидроакустических информационных систем"', 'Баз.ПАО ГИС'], 64: ['Базовая кафедра "Робототехники и автоматики"', 'Баз.РиА'], 99: ['Иная кафедра', 'ИК']}
    sms_names = [{'Первый семестр': 1},{'Второй семестр': 2},{'Третий семестр': 3},
                 {'Четвертый семестр': 4},{'Пятый семестр': 5},{'Шестой семестр': 6},
                 {'Седьмой семестр': 7},{'Восьмой семестр': 8},{'Девятый семестр': 9},
                 {'Десятый семестр': 10},]
    ans = [{'title': list(x.keys())[0], 'disciplines':[], 'exams': [], 'zaceths': [], 'div_zaceths': [], 'kursah': ''} for x in sms_names]
    print(ans)
    semester = {i:[] for i in range(1, 10)}
    exams = {i:[] for i in range(1, 10)}
    offsets = {i:[] for i in range(1, 10)}
    diff_offsets = {i:[] for i in range(1, 10)}
    course_works = {i:[] for i in range(1, 10)}
    subjects = conn.query(EtuStrPlan).filter(EtuStrPlan.plan_id == plan_id).all()
    for subj in subjects:
        a = conn.query(EtuSubject).filter(EtuSubject.plan_str_id == subj.etu_id).all()
        for inf_subj in a:
            summar = conn.query(Summary).filter(Summary.subject == subj.subject).all()
            summar = 'None' if not summar else summar[0].summary
            ans[inf_subj.sem - 1]['disciplines'].append({
                'title': subj.subject,
                'desctiption': summar[:min(200, len(summar))],
                'ze': inf_subj.ze,
                'hours': inf_subj.hours
            })
            ans[inf_subj.sem - 1]['disciplines'].sort(key=lambda x: x["hours"], reverse=True)
            if inf_subj.exam:
                ans[inf_subj.sem - 1]['exams'].append(subj.subject)
            if inf_subj.offset:
                ans[inf_subj.sem - 1]['zaceths'].append(subj.subject)
            if inf_subj.diff_offset:
                ans[inf_subj.sem - 1]['div_zaceths'].append(subj.subject)
            if inf_subj.course_work:
                ans[inf_subj.sem - 1]['kursah'] = subj.subject
    
    special = conn.query(Special).filter(Special.plan_id == plan_id).one()
    ans["departament"] = departments[special.department_id][1]
    ans["faculty"] = facs[special.fakultet_id]
    ans["study_form"] = study_form[special.study_form_id]
    d = {
        "semester": semester,
        "exams": exams,
        "offsets": offsets,
        "diff_offsets": diff_offsets,
        "course_works": course_works,
        "departament": departments[special.department_id][1],
        "faculty": facs[special.fakultet_id],
        "study_form": study_form[special.study_form_id]
    }
    return ans

if __name__ == '__main__':
    create = False
    Base.metadata.create_all(engine)
    
    #Title,SpecialtyId,DepartmentId,StudyFormId,StudyLevelId,StudyPeriod,FakultetId
    if create:
        with open('destination 2 (2).csv', 'r') as f:
            rows = csv.reader(f, delimiter=',')
            unq = set()
            ff = False
            for row in rows:
                ar = ''.join(row[i] for i in range(8) if i not in [0, 2])
                if ff and ar not in unq:
                    try:
                        insertion = Special(plan_id=row[0],name = row[1], specialty_id = int(row[2]),
                                                            department_id = int(row[3]),
                                                            fakultet_id = int(row[7]),
                                                            study_period = int(row[6]),
                                                            study_form_id = int(row[5]),
                                                            study_level_id = int(row[4]))
                        conn.add(insertion)
                        unq.add(ar)
                    except Exception as e:
                        print(e)
                    
                
                ff = True
            #print(unq)
        conn.commit()
        with open('res (4)', 'r') as f:
            jj = json.load(f)
        ff = False
        for k in jj:
            if ff:
                insertion = Vacancy(sphere=k, skills=str(jj[k])[1:-1].replace("'",'').replace(", ", ",").replace("\\xad", '-'))
                conn.add(insertion)
            ff = True

        with open('etu_str_plans.csv', 'r') as f:
            rows = csv.reader(f)
            next(rows)
            for row in rows:
                if row[4] == 'subject':
                    insertion = EtuStrPlan(etu_id = int(row[0]), subject=row[1], hours=int(row[2]), 
                                        plan_id = int(row[3]),type = row[4])
                    conn.add(insertion)
        conn.commit()

        for ins in addPriem(conn, engine, 'priem.json'):
            conn.add(ins)
            
        
        conn.commit()
        with open('hours.csv', 'r') as f:
            rows = csv.reader(f)
            next(rows)
            for row in rows:
                if not row[1].isalnum():
                    row[1] = 0
                ins = EtuSubject(subject_id = int(row[0]), ze = int(float(row[1])),
                                sem = int(row[2]), exam = row[3] == 'True',
                                offset = row[4] == 'True', diff_offset = row[5] == 'True',
                                course_work = row[6] == 'True', plan_str_id = int(row[8]),
                                hours = int(float(row[10])))
                conn.add(ins)
        conn.commit()
        with open('rpd.csv', 'r') as f:
            rows = csv.reader(f)
            next(rows)
            for row in rows:
                ins = Summary(summary = row[1], subject = row[2])
                conn.add(ins)
        conn.commit()

        URL = 'https://demo.pnvsh.n3dev.ru/api/v1/public/education_program/?educationType=additional&format=json&ordering=-created_at&pageSize=200&sort=&status=true&page={}'
        API_URL = 'https://demo.pnvsh.n3dev.ru'
        names = set()
        for i in range(1,40):
            response = requests.request('GET',URL.format(1)).text
            data = json.loads(response)
            for edu in data['results']:
                if edu['title'] in names:
                    continue
                ins = AddEdu(
                title = edu['title'],
                site = edu['site'],
                org_name = edu['organization']['shortTitle'],
                org_address = edu['organization']['address'],
                logo_url = API_URL + edu['organization']['logo']['url'],
                type = edu['type']['name'],
                edu_form = edu['educationForm']['name'],
                phone = edu['phone'],
                email = edu['email'],
                starts = edu['trainingStart'],
                cost = int(float(edu['costYear'])) if edu['costYear'] else 0,
                edu_len = edu['scopeMonths'] + 12*edu['scopeYears'])

                conn.add(ins)

                names.add(edu['title'])
        conn.commit()

    #get_edu_prog(6797, conn)
    #a = conn.query(AddEdu.org_name).all()
    #s = set(x for x in a)
    #print(s, len(s))
    #get_awesome_proff_sphere(6738,conn)
    get_edu_prog(6738, conn)
    conn.close()
