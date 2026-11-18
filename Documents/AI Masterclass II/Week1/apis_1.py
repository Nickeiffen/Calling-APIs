import requests
url = "https://pro-api.coinmarketcap.com/public-api/v1/simple/price?ids=1"
response = requests.get(url)



if response.status_code == 200:
    data = response.json()
    currency_id =data["data"][0]["id"]
    Price_ =data["data"][0]["price"]
    description =data["status"]
    print(f"The cryptocurrency price id {currency_id} is: USD {Price_}")
    print(f"Description/status:  {description}")

elif response.status_code == 401:
    print(f"API key is invalid or not yet active.")

elif response.status_code == 404:
    print(f"Value not found. Check the spelling.")

elif response.status_code == 429:
    print(f"Too many requests: Wait before trying again.")    
    
else:
    print(f"Error, request failed. Status: {response.status_code}")
    print(response.text)
