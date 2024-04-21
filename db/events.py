import db.uwuconfig as cfg
import requests as r
import json

class Event:
    def __init__(self, eventFormat: str = ""):
        self.eventFormat = eventFormat

def simplifyEvent(event):
    return { 'id': event['id'],  }

def getEvents(search: str, rnf: list):
    return json.loads(r.get(cfg.spb_pnvsh_url + f'/api/v1/public/event?isArchive=false&memberStatuses=enrollee,worker&search={search}&rnf={",".join(rnf)}').text)

def getRNFList():
    result = []
    a = json.loads(r.get(cfg.spb_pnvsh_url + f'/api/v1/public/rnf/list/').text)
    while a['next'] != None:
        result += a['results']
        a = json.loads(r.get(a['next']).text)
    
    result += a['results']
    return result

def getRNF(id):
    return json.loads(r.get(cfg.spb_pnvsh_url + f'/api/v1/public/rnf/{id}').text)

if __name__ == "__main__":
    #print(getEvents(""))
    print(getRNFList())
    #print(getRNF(5262))