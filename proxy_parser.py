import requests
from bs4 import BeautifulSoup

base_url = 'https://free-proxy-list.net/'

response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'lxml')
proxy_list = []
proxy_table = soup.find('table', {'class': 'table table-striped table-bordered'})
for row in proxy_table.find_all('tr')[1:]:
    columns = row.find_all('td')
    proxy_list.append(f"{columns[0].text}:{columns[1].text}")

for item in proxy_list[:50]:
    print(item)