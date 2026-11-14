import requests
import json
url = "https://pro-api.coinmarketcap.com/public-api/v1/simple/price?ids=1"
response = requests.get(url)

if response.status_code == 200:
   data = response.json() 
   
   for key, value in data.items():
      print(f"{key}: {value}")
   
   #print(json.dumps(data, indent=2))
else:
   print("error:", response.status_code)
