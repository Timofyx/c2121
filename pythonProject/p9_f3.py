import requests

res = requests.post("https://httpbin.org/post", data="Test data", headers={"h1": "Test title"})
print(res.text)