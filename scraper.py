import re
import requests
from bs4 import BeautifulSoup


def between_h2(url):
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    # extract Ads that mess with the article:
    for ad in soup.select('.contentAd'):
        ad.extract()
    out = {}
    tags = soup.find_all('h2')
    for tag in tags:
        current_header = tag.text
        while True:
            tag = tag.find_next_sibling()
            if not tag:
                break
            if tag.get('id', '') == 'moreResources':
                break # we don't want anything after this tag
            if tag.name == 'h2':
                current_header = tag.text
            else:
                out.setdefault(current_header, '')
                pattern=re.compile("([\ ]{2,})")
                text = re.sub(pattern,' ',str(tag.get_text(strip=False)))
                out[current_header] += text
    return out
def h2(url):
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    # extract Ads that mess with the article:
    for ad in soup.select('.contentAd'):
        ad.extract()

    out = {}
    tags = soup.find_all('h2')
    out = list(map(lambda tag: tag.text, tags))
    return out

    
