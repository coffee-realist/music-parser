from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re

song_name = "blinding lights the weeknd"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = f"https://genius.com/search?q={song_name}"
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
models = soup.find_all('a', class_='mini_card')
driver.get(models[0].get('href'))
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
text = []
for element in soup.find_all('div', class_="Lyrics__Container-sc-1ynbvzw-1 kUgSbL"):
    begin_index = 0
    txt = element.text
    for i in list(re.finditer(r'([^ \-(\[{\'A-ZА-Я]+[A-ZА-Я])', txt)):
        end_index = i.span()[1] - 1
        text.append(txt[begin_index:end_index])
        begin_index = end_index
    end = txt[begin_index:]
    if end:
        text.append(end)
print('\n'.join(text))
