from config import *
import requests

# payload = {'apikey': secret["HP"], 'text': 'Someone I know recently combined Maple Syrup.'}

# r = requests.get('http://api.idolondemand.com/1/api/sync/extractconcepts/v1', params=payload)

# print r.text
payload = {'some': 'data'}
cp = requests.post('https://api-us.clusterpoint.com/100581/Angel-hack/.json', data=payload)