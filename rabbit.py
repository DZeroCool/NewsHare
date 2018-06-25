# -*- coding: utf-8 -*-
import re, feedparser, time, datetime
from rabbit_content import *
from urllib.parse import urlparse

DEVELOPMENT_VERSION = 'beta'
DEPLOYMENT_ACTIVE = False
APACHE_DIR = '/var/www/html/' if DEPLOYMENT_ACTIVE else ''
RABBIT_DIR = '/home/supremeleader/' if DEPLOYMENT_ACTIVE else ''
DEGRADATION_DATE, EXPIRATION_DATE = 2, 9
now = datetime.datetime.now()
qualifications = {}
list_entries = []

def getAgeInDays(entry):
    try:
        then = datetime.datetime(*entry['published_parsed'][:7])
        delta = now - then
        return max(0, delta.days)
    except:
        return None

def qualification(entry,criteria):
    global qualifications
    isMatched = False
    title = entry['title']
    qualifications[title] = []
    age = getAgeInDays(entry)
    scalar = 1
    EXPIRATION_RANGE = EXPIRATION_DATE - DEGRADATION_DATE
    if age is not None and age >= DEGRADATION_DATE:
        scalar = (EXPIRATION_RANGE - min(EXPIRATION_RANGE - 1, age - DEGRADATION_DATE)) / EXPIRATION_RANGE
    score = 0
    scoring_weights = {}
    for criterion in criteria.split('\n'):
        criterion = criterion.split('#')[0].strip()
        if len(criteria) == 0: continue
        try:
            weight = float(criterion.split(":")[0].strip())
            target = criterion[criterion.find(':')+1:]
            scoring_weights[target] = weight*scalar
        except:
            pass
    weighted_criteria = []
    for key in scoring_weights.keys():
        weight = scoring_weights[key]
        weighted_criteria.append((weight, [token.strip().lower() for token in key.split(',')]))
    for weighted_criterion in sorted(weighted_criteria, reverse=True):
        weight, tokens = weighted_criterion[0], weighted_criterion[1]
        str_entry = str(entry).lower()
        if True:#try:
            foundAll = True
            for token in tokens:
                exclusion = False
                while token.startswith('-'):
                    exclusion = True
                    token = token[1:]
                if exclusion and re.search(token, str_entry):
                    return None
                if not re.search(token, str_entry):
                    foundAll = False
                    break
            if foundAll:
                isMatched = True
                score = score + weight
                qualifications[title].append((weight, token))
        else:#except:
            pass
    if not isMatched:
        return None
    return score

def html_link(text, address):
    return '<a href=' + address + '>'+text + '</a>'

def generate_results():
    from collections import Counter
    global qualifications
    all_titles = ""
    entries, setTitles = [], set()
    resultCount = 0
    for feed in feeds.split('\n'):
        feed = feed.strip()
        if len(feed) > 1:
           # print('Current feed:', feed)
            d = feedparser.parse(feed)
##            resultCount += len(d['entries'])
##            print('Entries present:', len(d['entries']))
            for entry in d['entries']:
                if entry['title'] not in setTitles:
                    entries.append(entry)
                    setTitles.add(entry['title'])
                    all_titles += " " + entry['title']
                    resultCount += 1
    output = ''
    for named_category in txt_categories:
        list_matches = []
        category = dict_categories[named_category]
        output += '<span id="' + ''.join(named_category.split()) + '">' + '<br><br>' + '*'*10 + ' ' + named_category.upper() + ' ' + '*'*10 + '<br>' + html_link('return to top', 'index.html') + '<br><br><br><br></span>'
        dict_entries = {}
        weighted_entries = []
        for entry in entries:
            score = qualification(entry, category)
            if score is None:
                continue
            dict_entries[entry['title']] = entry
            list_matches.append(entry)
            try:
                pp = entry['published_parsed']
                weighted_entries.append((score, (pp.tm_year, pp.tm_yday, pp.tm_hour*60+pp.tm_min), entry['title']))
            except:
                weighted_entries.append((score, (0,0,0), entry['title']))

        matchID = 0
        for weighted_entry in sorted(weighted_entries, reverse=True):
            entry = dict_entries[weighted_entry[2]]
            qualifiers = qualifications[entry['title']]
            output += '<big>' + html_link(entry['title'], entry['link']) + '</big><br>'
            try:
                output += entry['published'] + '<br>'
            except:
                pass
            try:
                output += entry['description'] + '<br>'
            except:
                pass
            output += 'Match ID: ' + str(matchID) + ' Score: %.2f' % weighted_entry[0] + ' source: '+ urlparse(entry['link']).netloc
            age = getAgeInDays(entry)
            if age is not None:
                output += ' age: %d days' % age if age is not 1 else ' age: 1 day'
            output += '<br>qualifiers: ' + ', '.join(['%.2f %s' % (qualifier[0], qualifier[1]) for qualifier in qualifiers]) + '<br>'
            output += '<br>'
            matchID += 1

        efficiency = 1 - matchID / resultCount
        output += 'Filter efficiency %.3f (%d matches/%d results)' % (100*efficiency, matchID, resultCount) + '<br>'
    freqOutput = ''
    freqOutput += 'Title Word Frequencies:\n'
    for v,k in sorted([(v,k) for k,v in Counter(all_titles.split()).items()])[::-1]:
        freqOutput += '%5d: %s\n' % (v,k)
    freqOutFile = open('Title Word Frequencies.txt', 'w', encoding='utf-8')
    freqOutFile.write(freqOutput)
    freqOutFile.close()
    return output


templateFile = open(RABBIT_DIR + 'template.html', 'r', encoding="utf-8")
template = templateFile.read()
templateFile.close()

index_html = template
index_html = index_html.replace('__development_version__', DEVELOPMENT_VERSION)
index_html = index_html.replace('__gohome__', 'index.html')
index_html = index_html.replace('__datetime__', time.asctime())
index_html = index_html.replace('__categories__', '<br>'.join([html_link(text.strip(), 'index.html#' + ''.join(text.split()).strip()) for text in txt_categories]))
index_html = index_html.replace('__output__', generate_results())

fileOutput = open(APACHE_DIR + 'index.html', 'w', encoding='utf-16')
fileOutput.write(index_html)
fileOutput.close()
