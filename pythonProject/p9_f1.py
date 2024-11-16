import urllib.request

opener = urllib.request.build_opener()
request = opener.open("https://httpbin.org/get")
print(request.read())