import csv
import json

with open("vacp.csv", "r") as f:
    rows = csv.reader(f)
    next(rows)
    for row in rows:
        sphere = row[0]
        exp = row[1]
        name = row[2]
        skills = row[3]
