import pandas as pd
from bs4 import BeautifulSoup
import lxml
import  urllib3
import requests
import sys


#Build Dictionary of Legal Terms

#Google search API Key: AIzaSyB7drVoOEtw21-m_uNyh-p-BHmvKTbljBo

file=open("dictionary_of_legal_terms.csv","w+")

url="http://www.uscourts.gov/glossary"
response=requests.get(url)
soup=BeautifulSoup(response.content,"lxml")
list_of_dt=soup.findAll("dt")
list_of_dd=soup.findAll("dd")

# print(list_of_dd[0].p.text)
print(list_of_dt[0].a["id"])
dict=""

for i in range(len(list_of_dd)):
    dict+=str(list_of_dt[i].a["id"]).strip().replace("\n","")+"\t"+str(list_of_dd[i].p.text).strip().replace("\n","")+"\n"
print(dict)

file.write(dict)
file.close()
