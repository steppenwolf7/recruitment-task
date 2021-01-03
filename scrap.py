import bs4
from bs4 import BeautifulSoup
import requests 
import pandas

url = "https://rpa.hybrydoweit.pl/#articles"

soup = BeautifulSoup(requests.get(url).text, features="html.parser")

#wydobycie ze znacznika "h3" tytułów 
t = soup.find(id="articles").find_all('h3') 
#utworznie pustego słownika
title = []

#pętla dodaje do listy "title" kolejne tytuły ze znacznika "h3"
for titles in t:
    result = titles.text.strip()
    title.append(result)
    
print(len(title))

i = soup.find(id="articles").find_all('li')
industry = []

for industries in i:
    result = industries.text.strip()
    industry.append(result)

print(len(industry))

l = soup.find(id="articles").find_all('a')
link = []

for links in l:
    result = links.get('href')
    link.append(result)

print(len(link))

#tworzenie tabeli z zebranych słowników 
data = pandas.DataFrame({'Link': link, 'Branża': industry,'Tytuł': title})
#zapis tabeli do pliku excel
data.to_excel("dane.xlsx", index=False)















