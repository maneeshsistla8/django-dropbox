import requests

payload = {'name':'Callum Hudson-Odoi', 'nation': 'England', 'stats':'https://www.whoscored.com/Players/350088/Show/Callum-Hudson-Odoi'}
r = requests.post("http://127.0.0.1:8000/players/", data=payload)

print(r.status_code)
