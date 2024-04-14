from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import json
import os

class UwURequestHandler(SimpleHTTPRequestHandler):
    def sendData(self, data):
        self.send_response(200)
        self.send_header('Content-type',  'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

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

        print("API CALL")
        print(cmds, args)

        if (len(cmds) == 1 and cmds[0] == "faculties"):
            data = {
                "faculties": [
                    { "id": 1, "title": "ФРТ" },
                    { "id": 2, "title": "ФЭЛ" },
                    { "id": 3, "title": "ФКТИ" },
                    { "id": 4, "title": "ФЭА" },
                    { "id": 5, "title": "ФИБС" },
                    { "id": 6, "title": "ИНПРОТЕХ" },
                    { "id": 7, "title": "ГФ" },
                    # { "id": 8, "title": "АСП" }
                ]
            }
            self.sendData(data)
        else:
            self.sendData({ "error": "unknown command" })
            
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