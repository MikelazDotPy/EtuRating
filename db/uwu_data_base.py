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

metadata = db.MetaData()
class Vacancy(Base):
    __tablename__ = 'vacancy'

    id = Column(Integer, primary_key=True)
    sphere = Column(Text)
    skills = Column(Text)

def getSpecialties(fakultet_id: int, session):
    select_all_query = session.query(Special).filter(Special.fakultet_id == fakultet_id).all()
    return select_all_query
    
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
    with open('res (4)', 'r') as f:
        jj = json.load(f)
    ff = False
    for k in jj:
        if ff:
            insertion = Vacancy(sphere=k, skills=str(jj[k])[1:-1].replace("'",'').replace(", ", ",").replace("\\xad", '-'))
            conn.add(insertion)
        ff = True
    
    conn.commit()
    conn.close()