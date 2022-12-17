import requests

# pip install requests
res = requests.get("https://news.ycombinator.com/")
# print(res.text)
# url = "http://www.google.com"
# response = requests.get(url)
# print(f"your request to {url} came with status code of {response.status_code}")

# -------------------------------------- headers -------------------------------------------------------------------
url = "https://icanhazdadjoke.com/"
response = requests.get(url, headers={"Accept": "application/json"})
print(response.text)     # it gives string
print(response.json())   # it converts the json into python code
print(type(response.json()))
print(response.json()["joke"])

# ------------------------------------------ query strings ---------------------------------------------------------
url = "https://icanhazdadjoke.com/search"
response = requests.get(url, headers={"Accept": "application/json"}, params={"term": "cat", "limit": 1})
data = response.json()
print(data["results"])

