 
import bs4
from bs4 import BeautifulSoup
import requests 
import pandas

url = "https://rpa.hybrydoweit.pl/#articles"

soup = BeautifulSoup(requests.get(url).text, features="html.parser")

t1 = soup.find(id="articles")
t = t1.find_all('h3') 
tittle = []

for tittles in t:
    result = tittles.text.strip()
    tittle.append(result)
    
print(len(tittle))

i1 = soup.find(id="articles")
i = i1.find_all('li')

industry = []

for industries in i:
    result = industries.text.strip()
    industry.append(result)

print(len(industry))


l1 = soup.find(id="articles")
l = l1.find_all('a')

link = []

for links in l:
    result = links.get('href')
    link.append(result)

print(len(link))


data = pandas.DataFrame({'Link': link, 'Branża': industry,'Tytuł': tittle})
data.to_excel("dane.xlsx", index=False)
#print(data)














