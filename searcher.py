from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import re

song_name = "applause"

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
for element in soup.find_all('a', class_="ReferentFragmentdesktop__ClickTarget-sc-110r0d9-0 cehZkS"):
    begin_index = 0
    txt = element.span.text
    for i in list(re.finditer(r'([^ \-(\[{\'A-ZА-Я]+[A-ZА-Я])', txt)):
        text.append(txt[begin_index:(i.span()[1] - 1)])
        begin_index = i.span()[1] - 1
    end = txt[begin_index:]
    if end:
        text.append(end)
print('\n'.join(text))


