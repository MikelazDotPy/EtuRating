from db.db_types import *
import itertools


translate_table = {
    "russian": "Русский язык",
    "maths": "Математика",
    "literatura": "Литература",
    "geography": "География",
    "informatics": "Информатика",
    "physics": "Физика",
    "history": "История",
    "biology": "Биология",
    "breaking_bad": "Химия",
    "society": "Обществознание",
    "english": "Английский язык"
}

class Exam:
    def __init__(self, type : str, points : int):
        self.type = type
        self.points = points

    def __str__(self) -> str:
        return f"<Exam '{self.type}': {self.points}>"
    
    def __repr__(self) -> str:
        return self.__str__()
                

def translateEGE(exams: list):
    newexams = []
    for exam in exams:
        newexams.append(Exam(translate_table[exam.type], exam.points))
    return newexams

def findEGE(session, exams: list, additional : int):
    s = exams[0].points + exams[1].points + exams[2].points + additional
    result = []

    for permutation in itertools.permutations(exams):
        q = session.query(Priem) \
            .filter(Priem.ege1 == permutation[0].type) \
            .filter(Priem.ege2 == permutation[1].type) \
            .filter(Priem.ege3 == permutation[2].type) \
            .filter(Priem.min1 <= permutation[0].points) \
            .filter(Priem.min2 <= permutation[1].points) \
            .filter(Priem.min3 <= permutation[2].points) \
            .filter(Priem.last_year <= int(s * 1.1)) \
            .all()
        result += q
    
    return list(map(lambda exam: exam.id, result))

def getSpecialtiesFromIDs(session, ids):
    return session.query(Special).filter(Special.id.in_(ids)).all()