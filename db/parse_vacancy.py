import csv
import json

def main():
    m = {}

    with open('vacancy.csv', 'r') as f:
        rows = csv.reader(f, delimiter=',')
        cnt = 0
        for row in rows:
            if cnt == 0:
                cnt = 1
                continue

            row[1] = row[1].strip()
            if not row[1] in m.keys():
                m[row[1]] = set()
            if row[4] != '/Не выявлено/' and row[1] != '':
                m[row[1]].add(row[4])

    m2 = {}

    for k, v in m.items():
        m2[k] = list(v)

    print(json.dumps(m2))

if __name__ == '__main__':
    main()