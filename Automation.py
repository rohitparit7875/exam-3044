import requests

# Example API call to get random user data
response = requests.get("https://randomuser.me/api/")
if response.status_code == 200:
    user = response.json()['results'][0]
    print("Name:", user['name']['first'], user['name']['last'])
    print("Email:", user['email'])
else:
    print("Failed to fetch data!")
