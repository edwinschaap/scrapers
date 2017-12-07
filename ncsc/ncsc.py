# python3
# Scrape advisories from ncsc.nl

import requests

def main():
    url = "https://www.ncsc.nl/dienstverlening/response-op-dreigingen-en-incidenten/beveiligingsadviezen/NCSC-2017-1058+1.00+Kwetsbaarheden+verholpen+in+Apple+iOS.html"
    response=requests.get(url)

    print(response)

if __name__ == '__main__':
    main()
