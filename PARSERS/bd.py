import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, Text
engine = db.create_engine('sqlite:///uwu.db')
conn = engine.connect()

metadata = db.MetaData()

subjects = Table('subjects', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', Text),
                 Column('hours', Integer),
                 Column('ze', Integer),
                 Column('summary', Text)
)

semesters = Table('semesters', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('number', Integer),
                  Column('subjects', db.ARRAY(Integer))
)

"""
directions = Table('directions', metadata,
                   Column('name', Text),
                   Column(''))
"""


if __name__ == '__main__':
    metadata.create_all(engine)
    #name="AiG", hours=144, ze=4, summary="hueta"
    #{'name':"AiG", 'hours':144, 'ze':4, 'summary':"hueta"}
    insertion = subjects.insert().values(name="AiG", hours=144, ze=4, summary="hueta")
    conn.execute(insertion)
    select_all_query = db.select(subjects)
    select_all_results = conn.execute(select_all_query)
    conn.commit()
    print(select_all_results.fetchall())