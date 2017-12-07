# python3
# Scrape advisories from ncsc.nl

import requests
from bs4 import BeautifulSoup

def getSoupFromUrl(url):
    response = requests.get(url)
    html = response.content
    return BeautifulSoup(html, "html.parser")

def main():
    url = "https://www.ncsc.nl/dienstverlening/response-op-dreigingen-en-incidenten/beveiligingsadviezen/NCSC-2017-1058+1.00+Kwetsbaarheden+verholpen+in+Apple+iOS.html"
    soup = getSoupFromUrl(url)

    print(soup)

if __name__ == '__main__':
    main()
