import json
import ijson
import csv
"""
with open('vacancy.json') as f:
    vacs = json.load(f)

#print(templates["vacancies"][0]["hardSkills"])
#"vacancy_name"
for i in range(len(vacs["vacancies"])):
    skills = [skill["hard_skill_name"] for skill in vacs["vacancies"][i]["hardSkills"]]
    if skills:
        print(f'{vacs["vacancies"][i]["vacancy_name"]}: {"; ".join(skills)}')
        print()
data = ijson.parse(open('vacancy_1.json', 'r'))
ans = []
i = 0
for prefix, event, value in data:
    if prefix == 'vacancies.item.vacancy_name':
        name = value
    if prefix == 'vacancies.item.hardSkills':
        skills = value
        if skills: ans += [f"{name}: {skills}"]
        print([i for i in ijson.items(event, prefix)])
    i += 1
    if i%1000 == 0 and ans != []:
        print()
        for e in ans:
            print(e)
        print()

for e in ans:
    print(e)
"""

def read_table(filename):
        answer = {}
        header = True
        with open(filename, newline='') as file:
            while True:
                row = file.readline()
                #print(row)
                #print()
                if not row:
                     break
                row = row.split('|')
                if header:
                    for i in range(len(row)):
                        if row[i] == 'vacancy_name':
                                name_idx = i
                        if row[i] == 'hardSkills':
                                skills_idx = i
                        if row[i] == 'position_requirements':
                                add_req_idx = i
                    header = False
                else:
                    answer[row[name_idx]] = row[add_req_idx]
                """
                elif row[skills_idx] != "[]":
                    #print(row[skills_idx].replace('""', '"')[1:-1])
                    js = json.loads(row[skills_idx].replace('""', '"')[1:-1])
                    skills = []
                    try:
                        for el in js:
                            try:
                                skills.append(el["hard_skill_name"])
                            except:
                                pass
                    except:
                        pass
                    #skills = [skill["hard_skill_name"] for skill in js]
                    if skills:
                        answer[row[name_idx]] = skills
                """

        return answer

d = read_table('vacancy.csv')
with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = "|", lineterminator="\r")
    for el in d:
        #file_writer.writerow([el, ','.join(d[el])])
        file_writer.writerow([el, d[el]])
