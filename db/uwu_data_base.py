import sqlalchemy as db
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, Text
import csv
import json

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///uwu.db', echo=False)
Session = sessionmaker(bind=engine)
conn = Session()
import sqlalchemy.orm
Base = sqlalchemy.orm.declarative_base()
metadata = db.MetaData()

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
    ze = Column(Integer)
    sem = Column(Integer)
    exam = Column(db.Boolean)
    exam = Column(db.Boolean)
    exam = Column(db.Boolean)
    exam = Column(db.Boolean)


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

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    
    #Title,SpecialtyId,DepartmentId,StudyFormId,StudyLevelId,StudyPeriod,FakultetId
    
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
    conn.close()