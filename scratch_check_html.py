import urllib.request

with urllib.request.urlopen('http://localhost:8089/index.html') as resp:
    data = resp.read()
    print('HTTP server returned bytes:', len(data))
    print(data.decode('utf-8')[-250:])
