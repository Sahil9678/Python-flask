import requests

url = 'http://127.0.0.1:5000/delete'

data = {"name" : "Sahil"}

response = requests.post(url , json= data)

print 'Response Code:', response.status_code