from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import random
from selenium.webdriver.chrome.options import Options

"""
platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
"""


def keyword(value):
    final = None
    try:
        # we need to prompt user to download webdriver-manager
        time.sleep(random.randint(1, 2))
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)
        key = value
        url = f'https://www.google.com/search?q={key}'
        driver.maximize_window()
        driver.get(url)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, "html.parser")

        names = soup.find('div', attrs={'id': 'result-stats'}).text
        tr = soup.find('div', attrs={'id': 'result-stats'})
        stopword = tr.find('nobr').text
        driver.quit()

        filtered = names.replace(f"{stopword}", "")
        filtered = filtered.replace(".", "")
        filtered = filtered.replace(",", "")

        numbers1 = [int(word) for word in filtered.split() if word.isdigit()]
        # ------------------------------------------------------------
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)
        key = value + " asuransi"
        url = f'https://www.google.com/search?q={key}'
        driver.maximize_window()
        driver.get(url)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, "html.parser")

        names = soup.find('div', attrs={'id': 'result-stats'}).text
        tr = soup.find('div', attrs={'id': 'result-stats'})
        stopword = tr.find('nobr').text
        driver.quit()

        filtered = names.replace(f"{stopword}", "")
        filtered = filtered.replace(".", "")
        filtered = filtered.replace(",", "")

        numbers2 = [int(word) for word in filtered.split() if word.isdigit()]

        oa = numbers2[0]/numbers1[0]
        if (oa > 0.25):
            oa = 100
        elif (0.25 >= oa >= 0.15):
            oa = 75
        elif (oa < 0.15):
            oa = 50

        aa = (numbers2[0]*2)/numbers2[0]
        if (aa > 1):
            aa = 100
        elif (1 >= aa >= 0.5):
            aa = 75
        elif (aa < 0.5):
            aa = 50

        final = 40*aa*oa/1000000
    except:
        final = 0

    return final
