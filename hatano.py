from urllib import request

response = request.urlopen('http://blog.livedoor.jp/nanjstu/')
content = response.read()
response.close()
html = content.decode()

title = html.split('<title')[1].split('</title')[0]

print(title)
