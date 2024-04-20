import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, Text
import csv
engine = db.create_engine('sqlite:///uwu.db')
conn = engine.connect()

metadata = db.MetaData()
#Title,SpecialtyId,DepartmentId,StudyFormId,StudyLevelId,StudyPeriod,FakultetID
Special = Table('special', metadata,
                Column('id', Integer, primary_key=True),
                Column('plan_id', Integer),
                Column('name', Text),
                Column('specialty_id', Integer),
                Column('department_id', Integer),
                Column('fakultet_id', Integer),
                Column('study_period', Integer),
                Column('study_form_id', Integer),
                Column('study_level_id', Integer))


def getSpecialties(fakultet_id: int):
    select_all_query = db.select(Special).filter_by(fakultet_id=fakultet_id)
    select_all_results = conn.execute(select_all_query)
    return select_all_results.fetchall()

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

    conn.commit()