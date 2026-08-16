import requests

url = "https://reqres.in/api/users/2"

custom_headers = {
    "User-Agent": "MyCustomBot/1.0",
    "x-api-key": "free_user_3HyDhCNxR6pfUt5YSXDe1GqhNFI"

}
def test_get_user():
    response = requests.get(url, headers=custom_headers)
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2

def test_create_user():
    response = requests.post(
        "https://reqres.in/api/users",
        headers=custom_headers,
        json={"name": "morgan", "job": "qa engineer"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "morgan"