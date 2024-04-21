import db.uwuconfig as cfg
import requests as r
import json
import db.uwu_data_base as db
from fuzzywuzzy import process

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

rnf = getRNFList()

def getSuitableRNFs(session, plan_id):
    q = session.query(db.EtuStrPlan.subject).filter(db.EtuStrPlan.plan_id == plan_id).all()
    res = []
    for x in q:
        arr = list(map(lambda x: x[0], process.extract(x[0], rnf, limit=3)))
        arr += res
    return res

if __name__ == "__main__":
    #print(getEvents(""))
    print(getRNFList())
    