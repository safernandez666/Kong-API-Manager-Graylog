import json
import requests
url = 'http://localhost:8000/frase/'


for i in range(30):
    print(i)

    r = requests.get(url + str(i))
    files = r.json()
    print(files)
