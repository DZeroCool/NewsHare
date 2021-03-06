# -*- coding: utf-8 -*-
import re, feedparser, time
from urllib.parse import urlparse

DEVELOPMENT_VERSION = 'beta'

feeds =  """http://feeds.bbci.co.uk/news/rss.xml
https://www.wired.com/feed/rss
https://www.theguardian.com/world/rss
https://www.theguardian.com/uk/rss
https://www.newyorker.com/feed/everything
https://www.politico.com/rss/politics08.xml
https://www.politico.com/rss/economy.xml
http://feeds.reuters.com/reuters/businessNews
http://feeds.reuters.com/news/wealth
http://feeds.reuters.com/Reuters/PoliticsNews
http://feeds.reuters.com/reuters/scienceNews
http://feeds.reuters.com/reuters/technologyNews
http://feeds.reuters.com/Reuters/worldNews
http://feeds.washingtonpost.com/rss/politics
http://feeds.washingtonpost.com/rss/world
http://feeds.washingtonpost.com/rss/lifestyle
http://www.wsj.com/xml/rss/3_7085.xml
http://www.wsj.com/xml/rss/3_7031.xml"""

categories, txt_categories, dict_categories = [], [], {}

def addCategory(name, criteria):
    global categories, txt_categories, dict_categories
    categories.append(criteria); txt_categories.append(name)
    dict_categories[name] = criteria

tech = """
20: feds 
25: trade
10: development
10: whatsapp
50: genetic 
50: genes 

25: google
10: amazon
5: uber
10: microsoft
10: tesla
15: musk
10: Apple 

5: startup
5: start-up
10: seattle
10: california
"""
addCategory('Technology', tech)

crypto = """
20: crypto
10: bitcoin
15: altcoins
15: alt coins"""
addCategory('Cryptography', crypto)

money = """
25: money
20: economy
25: stock-market
25: stockmarket
10: wealth
25: savings
40: gold"""
addCategory('Money', money)

space_stuff = """
65: NASA
25: astronomy
25: MIT
500: faster than light
500: faster-than-light
500: wormholes
500: space travel
250: space colonization
90: space, space travel, faster then light travel, mars colonization, aliens, wormholes #wut?
20: planets
"""
addCategory('Space', space_stuff)

climate = """
15: climate change
15: carbon
40: air pollution, toxic
"""
addCategory('Climate', climate)

world_affairs = """
10: nuclear
15: energy
25: trump
20: korea
5: pompeo
20: Russia
20: Italy 
15: trade, trump
35: sanctions
"""
addCategory('World Affairs', world_affairs)

matches, named_categories, qualifications = [], list(dict_categories.keys()), {}


def isMatched(entry,criteria):
    str_entry = str(entry).lower()
    for criterion in criteria.split('\n'):
        criterion = criterion.split('#')[0].strip()
        if len(criterion) == 0: continue
        try:
            target = criterion[criterion.find(':')+1:]
            tokens = [token.strip() for token in target.split(',')]
            if len(tokens) > 0:
                foundAll = True
                for token in tokens:
                    if not re.search(token, str_entry):
                        foundAll = False
                        break
                if foundAll:
                    return True
        except:
            pass
    return False

def qualification(entry,criteria):
    global qualifications
    title = entry['title']
    qualifications[title] = []
    score = 0
    scoring_weights = {}
    for criterion in criteria.split('\n'):
        criterion = criterion.split('#')[0].strip()
        if len(criteria) == 0: continue
        try:
            weight = float(criterion.split(":")[0].strip())
            target = criterion[criterion.find(':')+1:]
            scoring_weights[target] = weight
        except:
            pass
    weighted_criteria = []
    for key in scoring_weights.keys():
        weight = scoring_weights[key]
        weighted_criteria.append((weight, [token.strip().lower() for token in key.split(',')]))
    for weighted_criterion in sorted(weighted_criteria, reverse=True):
        weight, tokens = weighted_criterion[0], weighted_criterion[1]
        str_entry = str(entry).lower()
        try:
            foundAll = True
            for token in tokens:
                if not re.search(token, str_entry):
                    foundAll = False
                    break
            if foundAll:
                score = score + weight
                qualifications[title].append((weight, token))
        except: 
            pass
    return score

def html_link(text, address):
    return '<a href=' + address + '>'+text + '</a>'

def generate_results():
    global qualifications
    entries = []
    resultCount = 0
    for feed in feeds.split('\n'):
        feed = feed.strip()
        if len(feed) > 1:
           # print('Current feed:', feed)
            d = feedparser.parse(feed)
            resultCount += len(d['entries'])
##            print('Entries present:', len(d['entries']))
            for entry in d['entries']:
                entries.append(entry)
    output = ''
    for named_category in txt_categories:
        category = dict_categories[named_category]
        output += '<span id="' + ''.join(named_category.split()) + '">' + '<br><br>' + '*'*10 + ' ' + named_category.upper() + ' ' + '*'*10 + '<br>' + html_link('return to top', 'index.html') + '<br><br><br></span>'
        list_matches = list()
        for entry in entries:
            if isMatched(entry, category):
                list_matches.append(entry)

        dict_matches = {}
        weighted_matches = []
        for match in list_matches:
            score = qualification(match, category)
            dict_matches[match['title']] = match
            try:
                pp = match['published_parsed']
                weighted_matches.append((score, (pp.tm_year, pp.tm_yday, pp.tm_hour*60+pp.tm_min), match['title']))
            except:
                weighted_matches.append((score, (0,0,0), match['title']))

        matchID = 0
        for weighted_match in sorted(weighted_matches, reverse=True):
            match = dict_matches[weighted_match[2]]
            qualifiers = qualifications[match['title']]
            output += '<big>' + html_link(match['title'], match['link']) + '</big><br>'
            try:
                output += match['published'] + '<br>'
            except:
                pass
            try:
                output += match['description'] + '<br>'
            except:
                pass
            output += 'Match ID: ' + str(matchID) + ' Score: ' + str(weighted_match[0]) + ' source: '+ urlparse(match['link']).netloc + '<br>'
            output += 'qualifiers: ' + ', '.join(['%d %s' % (qualifier[0], qualifier[1]) for qualifier in qualifiers]) + '<br>'
            output += '<br>'
            matchID += 1

        efficiency = 1 - len(list_matches) / resultCount
        output += 'Filter efficiency %.3f (%d matches/%d results)' % (100*efficiency, len(list_matches), resultCount) + '<br>'
    return output

template = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>rssRabbit __development_version__</title>
</head>
<body>
<big><big><big><span
 style="color: rgb(15, 24, 253);">rss</span>Rabbit</big></big></big>
__development_version__<br>
<br>
Categories:<br>
__categories__<br>
<br>
Date/Time of Last Update: __datetime__ UTC<br>
<br>
__output__<br>
<br>
</body>
</html>
"""

index_html = template
index_html = index_html.replace('__development_version__', DEVELOPMENT_VERSION)
index_html = index_html.replace('__datetime__', time.asctime())
index_html = index_html.replace('__categories__', '<br>'.join([html_link(text.strip(), 'index.html#' + ''.join(text.split()).strip()) for text in txt_categories]))
index_html = index_html.replace('__output__', generate_results())

fileOutput = open('/var/www/html/index.html', 'w', encoding='utf-16')
fileOutput.write(index_html)
fileOutput.close()
