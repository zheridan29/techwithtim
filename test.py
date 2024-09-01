import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "hi/ace")
# response = requests.put(BASE + "hi/ace", {"likes": 10})
# response = requests.get(BASE + "video/1")
response = requests.put(BASE + "video/1", {"likes": 10, "name":"ace", "views":10000})

print(response.json())