import requests as req

targetUrl = 'http://dxvista.com/sandbox/api_previousresult'
data = {"patid":"20051427618","examid":"2"}
headers={'Accept':'*/*', 'Accept-Encoding':'gzip, deflate, br', 'Connection':'keep-alive'}
response = req.post(targetUrl, data=data, json=data, headers=headers)

print(response.content)