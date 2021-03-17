import json
import requests
url = 'http://localhost:8000/fras'


for i in range(100):
    r = requests.get(url)
    print("Send Request %s" % r.status_code)
