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
    "english": "Иностранный язык"
}

def translateEGE(data):
    newdata = []
    for i in data:
        newdata.append({ "value": i["value"], "type": translate_table[i["type"]] })
    return newdata

def findEGE(session, data, additional):
    s = data[0]["value"] + data[1]["value"] + data[2]["value"] + additional
    res = []

    for i in itertools.permutations(data):
        print("!!!!!! sum", s)
        print('############### check permutation', i)
        x = session.query(Priem) \
            .filter(Priem.ege1 == i[0]["type"]) \
            .filter(Priem.ege2 == i[1]["type"]) \
            .filter(Priem.ege3 == i[2]["type"]) \
            .filter(Priem.min1 <= i[0]["value"]) \
            .filter(Priem.min2 <= i[1]["value"]) \
            .filter(Priem.min3 <= i[2]["value"]) \
            .filter(Priem.last_year <= int(s * 1.1)) \
            .all()
        res += x
    
    return list(map(lambda x: x.id, res))

def getSpecialtiesFromIDs(session, ids):
    return session.query(Special).filter(Special.id.in_(ids)).all()