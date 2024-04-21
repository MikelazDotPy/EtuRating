import requests
import json

class Lectures:
    def initTable(session):
        session.execute("DROP TABLE IF EXISTS teacher")
        session.execute("DROP TABLE IF EXISTS course")
        session.execute("DROP TABLE IF EXISTS lecture_material")
        session.execute("CREATE TABLE IF NOT EXISTS teacher (id INTEGER PRIMARY KEY, name TEXT)")
        session.execute("CREATE TABLE IF NOT EXISTS course (id INTEGER PRIMARY KEY, name TEXT, teacher_id INTEGER)")
        session.execute("CREATE TABLE IF NOT EXISTS lecture_material (id INTEGER PRIMARY KEY, name TEXT, author TEXT, rating INTEGER, course_id INTEGER)")
    
        ETU_URL = "https://digital.etu.ru"
        university = json.loads(requests.get(ETU_URL + "/api/mobile/groups?year=current"))
        groups = []
        for faculty in university:
            for department in faculty:
                for group in department:
                    groups.append()


    def getTeachers(session):
        session.execute("SELECT * FROM teacher")