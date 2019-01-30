import requests

payload = {'name':'Gonzalo Higuain', 'nation': 'Argentina', 'stats':'https://www.whoscored.com/Players/19729/Show/Gonzalo-Higua%C3%ADn'}
r = requests.post("http://127.0.0.1:8000/players/", data=payload)
