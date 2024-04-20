import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, Text
engine = db.create_engine('sqlite:///uwu.db')
conn = engine.connect()

metadata = db.MetaData()
#Title,SpecialtyId,DepartmentId,StudyFormId,StudyLevelId,StudyPeriod,FakultetID
Special = Table('special', metadata,
                Column('id', Integer, primary_key=True),
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