import sqlalchemy as db
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, Text
import csv
import json

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

def getSpecialties(fakultet_id: int, session):
    select_all_query = session.query(Special).filter(Special.fakultet_id == fakultet_id).all()
    return select_all_query

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
            semester[inf_subj.sem].append({"subject":subj.subject, "hours":inf_subj.hours,
                                            "ze": inf_subj.ze, "summary":summar})
            if inf_subj.exam:
                exams[inf_subj.sem].append(subj.subject)
            if inf_subj.offset:
                offsets[inf_subj.sem].append(subj.subject)
            if inf_subj.diff_offset:
                diff_offsets[inf_subj.sem].append(subj.subject)
            if inf_subj.course_work:
                course_works[inf_subj.sem].append(subj.subject)
    d = {
        "semester": semester,
        "exams": exams,
        "offsets": offsets,
        "diff_offsets": diff_offsets,
        "course_works": course_works
    }
    return d

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

    get_edu_prog(6797, conn)

    conn.close()