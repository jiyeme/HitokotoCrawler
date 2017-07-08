import requests
r = requests.get('https://sslapi.hitokoto.cn/?encode=text')
print (r.text)