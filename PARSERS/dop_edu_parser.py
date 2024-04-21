import json
import requests
URL = 'https://demo.pnvsh.n3dev.ru/api/v1/public/education_program/?educationType=additional&format=json&ordering=-created_at&pageSize=200&sort=&status=true&page={}'
API_URL = 'https://demo.pnvsh.n3dev.ru'
for i in range(1,10):
    response = requests.request('GET',URL.format(1)).text
    data = json.loads(response)
    for edu in data['results']:
        title = edu['title']
        site = edu['site']
        org_name = edu['organization']['shortTitle']
        org_address = edu['organization']['address']
        logo_url = API_URL + edu['organization']['logo']['url']
        type = edu['type']['name']
        edu_form = edu['educationForm']['name']
        phone = edu['phone']
        email = edu['email']
        starts = edu['trainingStart']
        cost = int(edu['costYear'])
        edu_len = edu['scopeMonths'] + 12*edu['scopeYears']