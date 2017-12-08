# python3
# Scrape advisories from ncsc.nl

from bs4 import BeautifulSoup
import requests, gnupg, re, pprint

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
    advisory['version'] = re.findall(r'Versie\s*:(.+)', advisory['message'])[0].strip()
    advisory['probability'] = re.findall(r'Kans\s*:(.+)', advisory['message'])[0].strip()
    advisory['damage'] = re.findall(r'Schade\s*:(.+)', advisory['message'])[0].strip()
    advisory['publication_date'] = re.findall(r'Uitgiftedatum\s*:(.+)', advisory['message'])[0].strip()
    advisory['abstract'] = re.findall(r'Samenvatting(.+)Gevolgen', advisory['message'], re.DOTALL)[0]
    advisory['effects'] =  re.findall(r'Gevolgen(.+)Beschrijving', advisory['message'], re.DOTALL)[0]
    advisory['description'] =  re.findall(r'Beschrijving(.+)Mogelijke', advisory['message'], re.DOTALL)[0]
    advisory['solution'] =  re.findall(r'Mogelijke oplossingen(.+)Vrijwaringsverklaring', advisory['message'], re.DOTALL)[0]

    # Find all CVE IDs in the advisory
    advisory['CVE'] = set(re.findall(r'(CVE-\d{4}-(?:0\d{3}|[1-9]\d{3,}))', advisory['message']))

    return advisory

def getAdvisoryPages(max = 3):
    baseUrl = 'https://www.ncsc.nl/actueel/beveiligingsadviezen?r13_r1_r1:page='
    advisory_pages = []

    response = getSoupFromUrl(baseUrl + '1')
    for p in response.select('.advisoryitem h2 a'):
        advisory_pages.append('https://www.ncsc.nl'+p['href'])
        if max !=0 and len(advisory_pages) >= max:
            return advisory_pages
    return advisory_pages


def main():
    global gpg
    gpg = gnupg.GPG()
    advisories = []
    advisory_pages = getAdvisoryPages()
    for url in advisory_pages:
        advisories.append(parseAdvisoryPage(url))

    print('Advisories fetched: %d' % len(advisories))

if __name__ == '__main__':
    main()
