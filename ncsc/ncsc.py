# python3
# Scrape advisories from ncsc.nl

from bs4 import BeautifulSoup
import requests, gnupg, re

gpg = None

def getSoupFromUrl(url):
    response = requests.get(url)
    html = response.content
    return BeautifulSoup(html, "html.parser")

def parseAdvisoryPage(url):
    response = getSoupFromUrl(url)
    advisory = {}
    advisory['title'] = response.select('.advisoryitem h3')[0].contents[0].strip()
    advisory['message'] = response.select('.advisoryitem pre')[0].contents[0]
    advisory['verified'] = gpg.verify(advisory['message'])
    advisory['id'] = re.findall(r'Advisory ID\s*:(.+)', advisory['message'])[0].strip()
    return advisory

def main():
    global gpg
    gpg = gnupg.GPG()
    url = "https://www.ncsc.nl/dienstverlening/response-op-dreigingen-en-incidenten/beveiligingsadviezen/NCSC-2017-1058+1.00+Kwetsbaarheden+verholpen+in+Apple+iOS.html"
    advisory = parseAdvisoryPage(url)

    print(advisory['id'])

if __name__ == '__main__':
    main()
