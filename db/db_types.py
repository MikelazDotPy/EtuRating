import sqlalchemy as db
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, Text

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sqlalchemy.orm
Base = sqlalchemy.orm.declarative_base()

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

class Discipline(Base):
    __tablename__ = 'discipline'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    teachers = Column(String)

class Teacher(Base):
    __tablename__ =  'teacher'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = Column(String)

class Course(Base):
    __tablename__ =  'course'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    materials = Column(String)

class LectureMaterial(Base):
    __tablename__ =  'lecture_material'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    author = Column(String)
    rating = Column(Integer)