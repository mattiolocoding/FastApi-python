import requests

# errore per richiesta negativa , perche uso float
print(requests.put("http://127.0.0.1:8000/update/0?count=-1").json())
print(requests.put("http://127.0.0.1:8000/update/0?price=-1").json())


print(requests.put("http://127.0.0.1:8000/update/-1").json())

# e non puo superare 8 caratteri
print(requests.put("http://127.0.0.1:8000/update/0?name=SuperDuperHammer").json())
