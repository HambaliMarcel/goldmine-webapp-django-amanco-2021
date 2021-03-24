from bs4 import BeautifulSoup
import requests


def funding(value):
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    res = None
    try:
        html_content = session.get(
            f'https://www.crunchbase.com/organization/{value}').text
        soup = BeautifulSoup(html_content, 'html.parser')
        res = soup.find('span', attrs={
            'class': 'component--field-formatter field-type-money ng-star-inserted'}).text
        res = 0.25
    except:
        res = 0.125

    return res
