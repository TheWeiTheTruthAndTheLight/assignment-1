import requests
import functools
import re
from itertools import chain
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


def get(url, query):
    quoted_query = quote_plus(query)
    underscored_query = query.replace(' ', '_')
    full_url = '{}?q={}'.format(url, quoted_query)
    r = requests.get(full_url)
    status = r.status_code
    if status is 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup
    else:
        print('Error code: {}; URL: {}'.format(status, full_url))


def yahoo(query): return yahooParser(get('https://search.yahoo.com/search;', query))
def yahooParser(soup):
    matchURLsThatArentYahoosIP = re.compile("(?=^http.)(?!^http:\/\/98)")
    selectResultsTag           = lambda soup : soup.select("ol.searchCenterMiddle")[0]
    removeNewsAndSpecialLinks  = lambda soup : soup.select("div.wrapstar")+soup.select("div.algo")
    selectSearchResults        = lambda soup : removeNewsAndSpecialLinks(selectResultsTag(soup))
    removeInvalidURLs          = lambda url  : matchURLsThatArentYahoosIP.search(url)
    selectLinkTag              = lambda div  : div.find_all('a', href=True)
    selectLinkURL              = lambda link : link["href"]
    flatmap                    = lambda fun, lst : list(chain.from_iterable(map(fun,lst)))

    return list(filter(removeInvalidURLs,
                map(selectLinkURL,
                flatmap(selectLinkTag,
                        selectSearchResults(soup)))))


def google(query): return googleParser(get('https://www.google.com/search', query))
def googleParser(soup):
    matchNonSpecialResults = re.compile('^(?!News for|Images for).*$')
    selectResultTags       = lambda soup : soup.select('div#ires div.g h3.r a')
    removeSpecialResults   = lambda tags : filter(lambda tag: matchNonSpecialResults.search(tag.text), tags)
    selectLinkURL          = lambda link : link['href']
    trimURL                = lambda url  : url.strip('/url?q=').split('&')[0]

    return list(map(trimURL,
                map(selectLinkURL,
                    removeSpecialResults(selectResultTags(soup)))))


def bing(query): return bingParser(get('http://www.bing.com/search', query))
def bingParser(soup):
    return [t.h2.a['href'] for t in soup.find_all('li', 'b_algo')]


def search(query):
    return {
        'Bing'  : bing(query),
        'Google': google(query),
        'Yahoo' : yahoo(query),
    }
