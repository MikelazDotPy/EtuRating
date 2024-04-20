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
    engine = create_engine('sqlite:///db/uwu.db', echo=True)
    Session = sessionmaker(bind=engine)
    conn = Session()

    a = addPriem(conn, engine, "priem.json")
    print('\n'.join(list(map(lambda x: f'<({x.id}) ({x.name}) ({x.ege1}) ({x.ege2}) ({x.ege3}) ({x.min1}) ({x.min2}) ({x.min3}) ({x.last_year})>', a))))