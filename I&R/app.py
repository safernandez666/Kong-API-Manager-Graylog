with open('log.txt', 'r') as file:
    data = file.read().replace('\n', '')
string = "'client_ip': '"
ip = (data[data.index(string)+14:data.index(string)+26])
print (ip)