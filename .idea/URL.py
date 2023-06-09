import requests, json

url = "http://www.google.com"

json = requests(url)

text = json.text

print(text)