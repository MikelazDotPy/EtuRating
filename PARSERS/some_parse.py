import csv
csv.field_size_limit(200000)

a = []
s = set()
with open('rpd_str.csv', 'r') as f:
    rows = csv.reader(f)
    next(rows)
    for row in rows:
        a.append([row[0], row[2]])
        s.add(row[0])
with open('rpd.csv', 'r') as f:
    rows = csv.reader(f)
    next(rows)
    i = 0
    j = 0
    for row in rows:
        i += 1
        if row[0] in s:
            print(row[0])
            j += 1
    print()
    print(i, j)
print(len(s))
