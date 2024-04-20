import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, Text
import csv
import json

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
engine = create_engine('sqlite:///db/uwu.db', echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

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

Vacancy = Table('vacancy', metadata,
                Column('id', Integer, primary_key=True),
                Column('sphere', Text),
                Column('skills', Text))

def getSpecialties(fakultet_id: int, session):
    select_all_query = session.query(Special).filter(Special.fakultet_id == fakultet_id).all()
    return select_all_query
    
if __name__ == '__main__':
    metadata.create_all(engine)
    #Title,SpecialtyId,DepartmentId,StudyFormId,StudyLevelId,StudyPeriod,FakultetId
    
    with open('destination 2 (2).csv', 'r') as f:
        rows = csv.reader(f, delimiter=',')
        ff = False
        for row in rows:
            if ff:
                insertion = Special.insert().values(plan_id=row[0],name = row[1], specialty_id = int(row[2]),
                                                    department_id = int(row[3]),
                                                    fakultet_id = int(row[7]),
                                                    study_period = int(row[6]),
                                                    study_form_id = int(row[5]),
                                                    study_level_id = int(row[4]))
                conn.execute(insertion)
            
            ff = True
    
    with open('результат.txt', 'r') as f:
        jj = json.load(f)
    
    for k in jj:
        insertion = Vacancy.insert().values(sphere=k, skills=str(jj[k])[1:-1].replace("'","").replace(", ", ","))
        conn.execute(insertion)

    conn.commit()
