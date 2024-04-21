import csv

d = {}
with open('kaf.csv', 'r') as f:
    rows = csv.reader(f)
    ff = False
    for row in rows:
        if ff:
            d[int(row[0])] = int(row[3])
        ff = True

print(d)