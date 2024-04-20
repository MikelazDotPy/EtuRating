from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import json
import sqlalchemy
import os
import requests
from db import uwu_data_base as uwudb
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///db/uwu.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

faculties = [
    { "id": 30, "long_title": "Гуманитарный факультет", "title": "ГФ" },
    { "id": 38,	"long_title": "Институт фундаментального инженерного образования", "title": "ИФИО" },
    { "id": 42,	"long_title": "Институт инновационного проектирования и технологического предпринимательства", "title": "ИНПРОТЕХ" },
    { "id": 24,	"long_title": "Факультет радиотехники и телекоммуникаций", "title": "ФРТ" },
    { "id": 25,	"long_title": "Факультет электроники", "title": "ФЭЛ" },
    { "id": 26,	"long_title": "Факультет компьютерных технологий и информатики", "title": "ФКТИ" },
    { "id": 27,	"long_title": "Факультет электротехники и автоматики", "title": "ФЭА" },
    { "id": 28,	"long_title": "Факультет информационно-измерительных и биотехнических систем", "title": "ФИБС" },
]

faculties_dict = {}
for faculty in faculties:
    faculties_dict[faculty["id"]] = faculty

departments = {1: ['Автоматики и процессов управления', 'АПУ'], 2: ['"Информационные системы"', 'ИС'], 3: ['Биотехнических систем', 'БТС'], 4: ['Высшей математики', 'ВМ'], 5: ['"Алгоритмическая математика"', 'АМ'], 6: ['Вычислительной техники', 'ВТ'], 7: ['Инженерной защиты окружающей среды', 'ИЗОС'], 8: ['Инновационного менеджмента', 'ИМ'], 9: ['Иностранных языков', 'ИНЯЗ'], 10: ['Информационно-измерительных систем и технологий', 'ИИСТ'], 11: ['Фотоники', 'Фот'], 12: ['Корабельных систем управления', 'КСУ'], 13: ['Лазерных измерительных и навигационных систем', 'ЛИНС'], 14: ['Математического обеспечения и применения ЭВМ', 'МОЭВМ'], 15: ['Менеджмента и систем качества', 'МСК'], 16: ['Микрорадиоэлектроники и технологии радиоаппаратуры', 'МИТ'], 17: ['Микро- и наноэлектроники', 'МНЭ'], 18: ['Прикладной механики и инженерной графики', 'ПМИГ'], 19: ['Прикладной экономики', 'ПЭ'], 20: ['Радиотехнических систем', 'РС'], 21: ['Микроволновой электроники', 'МВЭ'], 22: ['Радиоэлектронных средств', 'РЭС'], 23: ['Робототехники и автоматизации производственных систем', 'РАПС'], 24: ['Систем автоматизированного проектирования', 'САПР'], 25: ['Систем автоматического управления', 'САУ'], 26: ['"Связи с общественностью"', 'СО'], 27: ['Телевидения и видеотехники', 'ТВ'], 28: ['Теоретических основ радиотехники', 'ТОР'], 29: ['Теоретических основ электротехники', 'ТОЭ'], 30: ['Физики', 'Физики'], 31: ['Физической химии', 'ФХ'], 32: ['Физической электроники и технологии', 'ФЭТ'], 33: ['Физического воспитания и спорта', 'ФВиС'], 34: ['Электроакустики и ультразвуковой техники', 'ЭУТ'], 35: ['Электронного приборостроения', 'ЭП'], 36: ['Электронных приборов и устройств', 'ЭПУ'], 37: ['Электротехнологической и преобразовательной техники', 'ЭТПТ'], 39: ['Безопасности жизнедеятельности', 'БЖД'], 40: ['Истории культуры, государства и права', 'ИКГП'], 41: ['Русского языка', 'РЯ'], 42: ['Социологии и политологии', 'СП'], 43: ['Философии', 'ФЛ'], 44: ['Экономики технологического предпринимательства', 'ЭТП'], 45: ['Базовая кафедра автоматизации исследований', 'Баз.АИ'], 46: ['Базовая кафедра "Интеллектуальные информационные технологии"', 'Баз.ИИТ'], 47: ['Медицинских технологий (базовая)', 'Баз.МТ'], 48: ['Базовая кафедра оптоэлектроники', 'Баз.ОЭ'], 49: ['Базовая кафедра радиоастрономии', 'Баз.РА'], 50: ['Базовая кафедра радиоэлектронных информационных систем и комплексов', 'Баз.РИСК'], 51: ['Базовая кафедра специальных средств радиоэлектроники', 'Баз.ССР'], 52: ['Базовая кафедра конструирования и производства судового электрооборудования', 'БККИПСЭ'], 53: ['Базовая кафедра технологии производства радиодеталей', 'БКТПР'], 54: ['Базовая кафедра конструирования и технологии электронной аппаратуры', 'Баз.КТЭА'], 55: ['Физики и современной технологии твердотельной электроники', 'Баз.ФТТЭ'], 58: ['Информационная безопасность', 'ИБ'], 59: ['Базовая кафедра "Вычислительные технологии"', 'Баз.ВТ'], 60: ['Базовая кафедра "Наноматериалы и нанотехнологии в радиоэлектронике"', 'Баз.ННР'], 61: ['Базовая кафедра "Медицинские информационные и биотехнические системы"', 'Баз.МИБТС'], 62: ['Базовая кафедра "Видеоинформационные системы"', 'Баз.ВИНС'], 63: ['Базовая кафедра "Программное и аппаратное обеспечение гидроакустических информационных систем"', 'Баз.ПАО ГИС'], 64: ['Базовая кафедра "Робототехники и автоматики"', 'Баз.РиА'], 99: ['Иная кафедра', 'ИК']}

study_form = {
    1: "Специалитет",
    2: "Бакалавриат",
    3: "Магистратура",
    7: "Аспирантура"
}

class UwURequestHandler(SimpleHTTPRequestHandler):
    def sendText(self, text):
        self.send_response(200)
        self.send_header('Content-type',  'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'Authorization, Content-Type')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.end_headers()
        self.wfile.write(text)
        print(f"{bcolors.OKGREEN}{self.date_time_string()} {bcolors.OKBLUE}send: '{text}'{bcolors.ENDC}")

    def sendData(self, data):
        self.sendText(json.dumps(data).encode())

    def doEGE(self, cmds, args):
        pass

    def doSpecialty(self, cmds, args):
        sp = uwudb.getSpecialties(int(cmds[1]), session)
        self.sendData(list(map(lambda x: { "id": x.id, "plan_id": x.plan_id, "name": x.name, "specialty_id": x.specialty_id, "department_id": x.department_id, "department": departments[x.department_id][1],"faculty_id": x.fakultet_id, "faculty": faculties_dict[x.fakultet_id]["title"], "study_period": x.study_period, "type": study_form[x.study_form_id], "study_level_id": x.study_level_id }, sp)))
        '''
        self.sendData(list(map(lambda x:
          { "title": x[0], "id": x[1], "department": departments[x[2]][1], "study_form": study_form[x[3]] }  
        , sp)))
        '''

    def doAPI(self):
        cmd = self.path.split('/')[2:]
        arglist = list(map(lambda x: list(map(lambda y: (y[:y.find('=')], y[y.find('=') + 1:]), x[x.find('?'):][1:].split('&'))), cmd))

        args = []
        cmds = []

        for arg in arglist:
            m = {}
            for x in arg:
                m[x[0]] = x[1]
            args.append(m)

        for x in cmd:
            if (x.find('?') == -1):
                cmds.append(x)
            else:
                cmds.append(x[:x.find('?')])

        print(cmds, args)

        if (len(cmds) == 1 and cmds[0] == "faculties"):
            self.sendData(faculties)
        elif (len(cmds) == 1 and cmds[0] == "ege"):
            self.doEGE(cmds, args)
        elif (len(cmds) == 2 and cmds[0] == "faculties"):
            self.doSpecialty(cmds, args)
        else:
            self.sendData({ "message": "ECHO", "cmds": cmds, "args": args })
            
    def do_GET(self):
        if (self.path.find('/api/') == 0):
            self.doAPI()
        else:
            super().do_GET()

if __name__ == '__main__':    
    os.chdir(os.path.dirname(__file__) + "/root/")
    
    server_address = ('', 8000)
    httpd = ThreadingHTTPServer(server_address, UwURequestHandler)
    httpd.serve_forever()

    Session.remove()