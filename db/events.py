import json
import requests as r
import uwuconfig as cfg

class Event:
    def __init__(self, id, name, tags):
        self.id = id
        self.name = name
        self.tags = tags

class Tag:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'\{ "id": {self.id}, "name": "{self.name}" \}'

    def __repr__(self):
        return self.__str__()

def getTags():
    js = json.loads(r.get(cfg.spb_pnvsh_url + "/api/v1/public/rnf/list/").text)
    l = []

    while (js["next"] != None):
        data = js["results"]
        for i in data:
            l.append(Tag(i["id"], i["name"]))

        js = json.loads(r.get(js["next"]).text)
    return l

if __name__ == "__main__":
    x = getTags()
    print(x)
