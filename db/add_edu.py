from db.db_types import *

def castAddEduToDict(obj):
    return {
        'id': obj.id,
        'title': obj.title,
        'site': obj.site,
        'org_name': obj.org_name,
        'org_address': obj.org_address,
        'logo_url': obj.logo_url,
        'type': obj.type,
        'edu_form': obj.edu_form,
        'phone': obj.phone,
        'email': obj.email,
        'starts': obj.starts,
        'cost': obj.cost,
        'edu_len': obj.edu_len
    }

def getAdditionalEducation(session):
    q = session.query(AddEdu) \
        .all()
    
    return list(map(castAddEduToDict, q))