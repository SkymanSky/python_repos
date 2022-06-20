import requests

#API çağrısı yap ve yanıtı sakla.
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'Accept':'application/vnd.github.v3+json'}
r=requests.get(url,headers=headers)
print(f"Status code: {r.status_code}")

#API yanıtını bir değişkende sakla.
response_dict=r.json()

#Sonuçları işle.
print(response_dict.keys())