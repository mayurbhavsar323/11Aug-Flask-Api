
import requests
# import json

BASE = "http://127.0.0.1:5000/"
response = requests.get(BASE + "video/1")
print(response.json())

# response = requests.get(BASE + "demo/Yash")
# response = requests.put(BASE + "video/1", {"likes":10})
