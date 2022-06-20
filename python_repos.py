import requests

#API çağrısı yap ve yanıtı sakla.
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'Accept':'application/vnd.github.v3+json'}
r=requests.get(url,headers=headers)
print(f"Status code: {r.status_code}")

#API yanıtını bir değişkende sakla.
response_dict=r.json()
print(f"Total repositories: {response_dict['total_count']}")

#Sonuçları işle.
#print(response_dict.keys())

#Repolar hakkındaki bilgileri incele.
repo_dicts=response_dict['items']
print(f"Repositories Returned: {len(repo_dicts)}")

#İlk repoyu incele.
repo_dict=repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)