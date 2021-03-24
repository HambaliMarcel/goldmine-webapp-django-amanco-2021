from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import random
from selenium.webdriver.chrome.options import Options


def hc(value):
    head = None
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        url = f'http://www.linkedin.com/company/{value}/'
        driver.maximize_window()
        driver.get(url)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, "html.parser")
        names = soup.find(
            'a', attrs={'class': 'top-card__right-column-link'}).text
        driver.quit()
        filtered = names.replace(",", "")
        numbers1 = [int(word) for word in filtered.split() if word.isdigit()]
        head = numbers1[0]
        if (head < 20):
            head = 0
        elif (100 > head >= 20):
            head = 0.175
        elif (head >= 100):
            head = 0.35
    except:
        driver.quit()
        head = 0

    return head
