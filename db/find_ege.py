from db_types import *
import itertools

def translateEGE(data):
    return data

def findEGE(session, data):
    data = sorted(data)
    
    s = data[0]["value"] + data[1]["value"] + data[2]["value"]
    res = []

    for i in itertools.permutations(data):
        x = session.query(Priem) \
            .filter(Priem.ege1 == i[0]["type"]) \
            .filter(Priem.ege2 == i[1]["type"]) \
            .filter(Priem.ege3 == i[2]["type"]) \
            .filter(Priem.min1 >  i[0]["value"]) \
            .filter(Priem.min2 >  i[1]["value"]) \
            .filter(Priem.min3 >  i[2]["value"]) \
            .filter(Priem.last_year >= int(s * 1.1)) \
            .all()
        if len(x) > 0:
            res += x
    
    return list(map(lambda x: x.id, res))

def getSpecialtiesFromIDs(session, ids):
    return list(map(lambda x: session.query(Special).filter(Special.id.in_(ids)).all()[0]))