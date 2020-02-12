# get_data.py

import requests
import json

print("REQUESTING SOME DATA FROM THE INTERNET...")

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
print("URL:", request_url)

response = requests.get(request_url)
print(type(response))
#print(dir(response))

print(response.status_code)
#print(response.text)
print(type(response.text))

parsed_response = json.loads(response.text)
print(type(parsed_response))

total = 0
for d in parsed_response["students"]:
    total = total + int(d["finalGrade"])

#total = [int(d["finalGrade"] for d in parsed_response["students"]]

avg = total / len(parsed_response["students"])

print(avg)

#print(parsed_response["name"])

