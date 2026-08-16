import requests

url = "https://reqres.in/api/users/2"

custom_headers = {
    "User-Agent": "MyCustomBot/1.0",
    "x-api-key": "free_user_3HyDhCNxR6pfUt5YSXDe1GqhNFI"

}
response = requests.get(url, headers=custom_headers)

print(response.status_code)
print(response.json())
