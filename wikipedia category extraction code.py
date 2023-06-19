import requests
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/Category:21st-century_Cameroonian_male_singers'


# Open a file for writing
with open('French_singers.txt', 'a') as file:


   # Loop through all pages
   while url:
       response = requests.get(url)
       html = response.content
       soup = BeautifulSoup(html, 'html.parser')


       # Locate the div container
       div_container = soup.find('div', {'class': 'mw-content-ltr'})


       # Extract names and write them to the file
       for a in div_container.find_all('a', href=True):
           href = a['href']
           if '/wiki/' in href and ':' not in href:
               name = a.text
               file.write(name + '\n')


       # Find the <a> element that represents the next page link
       next_page_link = div_container.find('a', text='next page')
       if next_page_link:
           next_page_href = next_page_link['href']
           url = "https://en.wikipedia.org/" + next_page_href
       else:
           url = None


print('Names saved')