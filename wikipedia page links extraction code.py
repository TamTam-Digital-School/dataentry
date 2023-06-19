import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/Category:Footballers_in_Bolivia_by_club"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


links = []
for link in soup.find_all("a"):
   href = link.get("href")
   if href and "/wiki/" in href:
       links.append(href)


with open("footbolivia_links.txt", "w") as f:
   f.write("\n".join(links))