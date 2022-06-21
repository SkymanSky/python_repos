import requests
from plotly.graph_objs import Bar
from plotly import offline

#API çağrısı yap ve yanıtı sakla.
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'Accept':'application/vnd.github.v3+json'}
r=requests.get(url,headers=headers)
print(f"Status code: {r.status_code}")

#API yanıtını bir değişkende sakla.
response_dict=r.json()
repo_names,stars = [],[]
print(f"Total repositories: {response_dict['total_count']}")


#Sonuçları işle.
#print(response_dict.keys())

#Repolar hakkındaki bilgileri incele.
repo_dicts=response_dict['items']
print(f"Repositories Returned: {len(repo_dicts)}")
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#Görselleştirme yap.
data=[{
    'type':'bar',
    'x':repo_names,
    'y':stars,
}]

my_layout={
    'title':'Most-Starred Python Projects on GitHub ',
    'xaxis':{'title':'Repository'},
    'yaxis':{'title':'Stars'}
}

fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='python_repos.html')