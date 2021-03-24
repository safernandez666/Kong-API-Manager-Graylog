import json
import requests
import time

url = 'http://api.local:8000/frase/'

if __name__ == '__main__':
    try:
        main()
        for i in range(100):
            print("Request Numero %d " % i)
            r = requests.get(url + str(i))
            files = r.json()
            print(files)
            time.sleep(3)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)