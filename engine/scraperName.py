from bs4 import BeautifulSoup
from engine.models import results
from .models import results, breaker
from .scraperKey import keyword
from .scraperFun import funding
from .scraperHead import hc
from django.shortcuts import redirect, render
import requests
import time
import random


def scrapeName(request, pages):

    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    page = pages
    while page < 679:
        broker = breaker.objects.get(username=request)
        if (broker.status == "stop"):
            print(broker.status)
            break
        else:
            html_content = session.get(
                f'https://kemenperin.go.id/direktori-perusahaan?what=&prov=&hal={page}').text
            soup = BeautifulSoup(html_content, 'html.parser')
            for tr in soup.find_all('tr')[1:]:
                broker = breaker.objects.get(username=request)
                if (broker.status == "stop"):
                    print(broker.status)
                    break
                try:
                    names = tr.find_all('b')
                    tds = tr.find_all('td')
                    name = names[0].text
                    query = tds[1].text
                    loc = query.replace(f"{name}", " ")

                    try:
                        telp = loc.split("Telp.", 1)[1]
                    except:
                        telp = "N/A"

                    loc = loc.replace(f"Telp.{telp}", " ")
                    try:
                        exist = results.objects.get(number=tds[0].text)
                    except:
                        resKey = keyword(name)
                        resFun = funding(name)
                        resHead = hc(name)
                        raw = resFun+resHead+resKey
                        likelihood = "{:.0%}".format(raw)

                        # print(tds[0].text, " | ", name, " | ", loc,  " | ", telp, " | ",
                        #       tds[2].text, " | ", resKey, resFun, resHead, " | ", likelihood)
                        try:
                            obj = results(number=tds[0].text,
                                          name=name,
                                          loc=loc,
                                          sector=tds[2].text,
                                          contact=telp,
                                          likelihood=likelihood
                                          )
                            obj.save()

                        except:
                            continue
                except:
                    continue

        page += 1
        time.sleep(random.randint(1, 2))

    return None
