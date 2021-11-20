from bs4 import BeautifulSoup
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(START_URL, verify=False)
soup = BeautifulSoup(page.content, "html.parser")
table = soup.find("table")
body = table.find("tbody")

star_data = []
Name = []
Distance = []
Mass = []
Radius = []

for tr_tag in body.find_all("tr"):
    td_tags = tr_tag.find_all("td")
    row = [i.text.rstrip() for i in td_tags]
    star_data.append(row)

for i in range(1, len(star_data)):
    Name.append(star_data[i][1])
    Distance.append(star_data[i][3])
    Mass.append(star_data[i][5])
    Radius.append(star_data[i][6])

dict = {"Star_Name": Name, "Distance": Distance, "Mass": Mass, "Radius": Radius}
df = pd.DataFrame(dict)
df.to_csv("127.csv")
