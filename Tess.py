import requests
import json
import pprint
API = "https://api.safone.me/tmdb"
NAME = input("enter name")
params = {"query" : NAME}

response = requests.get(API,params)
 data = json.loads(response.text)
  title = data['name']
  rating = data['rating']
  poster link = data['poster']
  
  print(title)
  print(data)
  print(poster)
  
  
