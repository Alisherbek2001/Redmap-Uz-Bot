import requests
from environs import Env
env = Env()
env.read_env()
BASE_URL = env.str('URL')
# def create_user(fullname,telegram_id,phone):
#     response = requests.post(f"{BASE_URL}/api/user/",data={'fullname':fullname,'telegram_id':telegram_id,'phone':phone})
#     return 'OK'

def get_hayvon(region):
    hayvonlar = []
    response = requests.get(f"{BASE_URL}api/hayvon/")
    hayvon_data = response.json()
    for i in hayvon_data:
        if i['region']==region:
            hayvonlar.append(i)
    return hayvonlar

def get_osimlik(region):
    osimliklar = []
    response = requests.get(f"{BASE_URL}api/osimlik/")
    osimlik_data = response.json()
    for i in osimlik_data:
        if i['region']==region:
            osimliklar.append(i)
    return osimliklar