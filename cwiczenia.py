import requests
from pprint import pprint

url = 'https://mate-django-backend.herokuapp.com/api/v1/category/'
r = requests.get(url)

dir(r)
[el for el in dir(r) if '_' not in el]

r.status_code
r.text
r.json()
pprint(r.json())

"""
Sprawdzić później wszystkie metody i pola
"""
type(r.content)

r = requests.get(url)
payload = {'name': 'egzotyczne'}
r = requests.post(url, json=payload)

url_local = 'http://127.0.0.1:8000/api/v1/question/'
r_local = requests.get(url_local)
r_local.status_code
pprint(r_local.json())

payload_local = {'pub_date': '2021-03-05T21:35:53Z',
                 'question_text': 'czy wam się podoba???'}
r_local = requests.post(url_local, json=payload_local)

url_local = 'http://127.0.0.1:8000/api/v1/question/'
r_local = requests.get(url_local)
pprint(r_local.json())
