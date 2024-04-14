import csv
"""
class DirectionSummary:
    def __init__(self, direction, summary, edu_prog = None):
        self.direction = direction
        self.summary = summary
        self.edu_prog = edu_prog if edu_prog else direction

    def __str__(self) -> str:
        return f"Направление: {self.direction}  ОП: {self.edu_prog}"

class SummaryTag(DirectionSummary):
    def __init__(self, direction, summary, tags: str, edu_prog=None):
        super().__init__(direction, summary, edu_prog)
        self.tags = tags

    def __str__(self) -> str:
        return super().__str__() + f"\nТэги: {self.tags}"
"""

def check_file_name(filename):
    return filename.endswith(".csv")

def read_table(filename):
    answer = {}
    if not check_file_name(filename):
        print("incorrect file extension. stop")
        exit(1)
    try:
        with open(filename, newline='') as file:
            rows = csv.reader(file, delimiter=';')
            for row in rows:
                answer[row[0]] = row[1]
    except Exception as error:
        print("error work with table: {}. stop".format(error))
        exit(1)

    return answer

        