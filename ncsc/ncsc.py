# python3
# Scrape advisories from ncsc.nl

import requests
from bs4 import BeautifulSoup

def getSoupFromUrl(url):
    response = requests.get(url)
    html = response.content
    return BeautifulSoup(html, "html.parser")

def parseAdvisoryPage(url):
    response = getSoupFromUrl(url)
    advisory = {}
    advisory['title'] = response.select('.advisoryitem h3')[0].contents[0].strip()

    return advisory

def main():
    url = "https://www.ncsc.nl/dienstverlening/response-op-dreigingen-en-incidenten/beveiligingsadviezen/NCSC-2017-1058+1.00+Kwetsbaarheden+verholpen+in+Apple+iOS.html"
    advisory = parseAdvisoryPage(url)

    print(advisory)

if __name__ == '__main__':
    main()
