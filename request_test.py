import requests

r = requests.get('https://httpstatuses.com/')
print(r.status_code)
print(r.headers)