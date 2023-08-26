import  scraper
from pprint import pprint

url = 'https://www.gob.bo/tramite/231'

heads = scraper.h2(url)

pprint(heads)

out  = scraper.between_h2(url)

pprint(out, width=120)
