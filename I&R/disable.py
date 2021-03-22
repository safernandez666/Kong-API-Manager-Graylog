#!/usr/bin/env python3
import json
import sys
import time
import requests

url = 'http://kong:8001/services/MyAPI/plugins'

# Function that prints text to standard error
def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Funcion Extract IP
def extract_ip():
    with open('log.txt', 'r') as file:
        data = file.read().replace('\n', '')
    string = "client_ip"
    ip = (data[data.index(string)+11:data.index(string)+26]).strip('"\'')
    return ip

# Count Time
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

# Block IP
def bloqueo(client_ip):
    data = {'name':'ip-restriction',
            'config.deny':client_ip}
    r = requests.post(url, data)
    data = r.json()
    sys.stdout.write('Bloqueado: %s' % data['config']['deny'])
    return data

# Delete API Manager Rule
def eliminar(data):
    sys.stdout.write('El ID del Plugin es: %s' % data['id'])
    sys.stdout.write('Desbloqueo: %s' % data['config']['deny'])
    r = requests.delete(url + '/' + data['id'])
    return r.status_code

# Main Program
if __name__ == "__main__":
    temp = sys.stdout #store original stdout object for later
    sys.stdout = open('log.txt','w') #redirect all prints to this log file
    # Print out all input arguments.
    sys.stdout.write("All Arguments Passed In: " + ' '.join(sys.argv[1:]) + "\n")

    # Turn stdin.readlines() array into a string
    std_in_string = ''.join(sys.stdin.readlines())

    # Load JSON
    event_data = json.loads(std_in_string)
    print (event_data)
    # Extract some values from the JSON.
    sys.stdout.write("Values from JSON: \n")
    sys.stdout.write("Event Definition ID: " + event_data["event_definition_id"] + "\n")
    sys.stdout.write("Event Definition Title: " + event_data["event_definition_title"] + "\n")
    sys.stdout.write("Event Timestamp: " + event_data["event"]["timestamp"] + "\n")

    # Extract Message Backlog field from JSON.
    sys.stdout.write("\nBacklog:\n")
    for message in event_data["backlog"]:
        for field in message.keys():
            sys.stdout.write("Field: " + field + "\t")
            sys.stdout.write("Value: " + str(message[field]) + "\n")
    sys.stdout.close()
    sys.stdout = temp

    # Extraigo Direccion IP del log.txt
    ip = extract_ip()
    id = bloqueo(ip)
    countdown(10)
    eliminar(id)
    exit(0)
