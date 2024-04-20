from db_types import *
import json

def addPriem(conn, engine, filename):
    r = []
    with open(filename) as f:
        s = f.read()
        l = json.loads(s)
        for x in l:
            p = Priem(
                id   = conn.query(Special.id).filter(Special.name == x["Направление"]).all()[0][0],
                name = x["Направление"],
                ege1 = x["Предмет 1"],
                ege2 = x["Предмет 2"],
                ege3 = x["Предмет 3"],
                min1 = x["Мин. балл 1"],
                min2 = x["Мин. балл 2"],
                min3 = x["Мин. балл 3"],
                last_year = x["Балл"]
            )
            r.append(p)
    return r

if __name__ == "__main__":
    print(addPriem(conn, engine, "priem.json"))