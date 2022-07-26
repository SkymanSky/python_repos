import requests
from plotly import offline

#API çağrısı yap ve yanıtı sakla.
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'Accept':'application/vnd.github.v3+json'}
r=requests.get(url,headers=headers)
print(f"Status code: {r.status_code}")

#API yanıtını bir değişkende sakla.
response_dict=r.json()
repo_links,stars, labels = [],[],[]
print(f"Total repositories: {response_dict['total_count']}")


#Sonuçları işle.
#print(response_dict.keys())

#Repolar hakkındaki bilgileri incele.
repo_dicts=response_dict['items']
print(f"Repositories Returned: {len(repo_dicts)}")
for repo_dict in repo_dicts:
    repo_name=repo_dict['name']
    repo_url=repo_dict['html_url']
    repo_link=f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    owner=repo_dict['owner']['login']
    description=repo_dict['description']
    label=f"{owner}<br />{description}"
    labels.append(label)

#Görselleştirme yap.
data=[{
    'type':'bar',
    'x':repo_links,
    'y':stars,
    'hovertext':labels,
    'marker':{
        'color':'rgb(60,100,150)',
        'line':{'width':1.5,'color':'rgb(25,25,25)'}
    },
    'opacity':0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },

}

fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='python_repos.html')