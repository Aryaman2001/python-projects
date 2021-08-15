import requests
import pandas
from bs4 import BeautifulSoup

r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

c = r.content
soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("div", {"class": "propertyRow"})
#print(all[0].find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", ""))

l=[]
for item in all:
    d={}
    d["Address"] = (item.find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", ""))
    d["Locality"] = (item.find_all("span", {"class", "propAddressCollapse"})[0].text)
    d["Price"] = (item.find_all("span", {"class", "propAddressCollapse"})[1].text)
    try:
        d["Beds"] = (item.find("span", {"class", "infoBed"}).find("b").text)
    except:
        d["Beds"] = (None)

    try:
        d["Area"] = (item.find("span", {"class", "infoSqFt"}).find("b").text)
    except:
        d["Area"] = (None)

    try:
        d["Full Baths"] = (item.find("span", {"class", "infoValueFullBath"}).find("b").text)
    except:
        d["Full Baths"] = (None)

    try:
        d["Half Baths"] = (item.find("span", {"class", "infoValueHalfBath"}).find("b").text)
    except:
        d["Half Baths"] = (None)

    l.append(d)
    
df=pandas.DataFrame(l)
print(df)


