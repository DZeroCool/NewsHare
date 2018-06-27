feeds =  """http://feeds.bbci.co.uk/news/rss.xml
http://feeds.bbci.co.uk/news/rss.xml?edition=us
http://feeds.bbci.co.uk/news/rss.xml?edition=int
http://hbswk.hbs.edu/stories-rss.aspx
http://www.eurekalert.org/rss/technology_engineering.xml
https://spectrum.ieee.org/rss/aerospace/fulltext
https://spectrum.ieee.org/rss/fulltext
https://www.wired.com/feed/rss
https://www.wired.com/feed/category/ideas/latest/rss
http://www.feedbucket.com/?src=https%3A%2F%2Fwww.wired.com%2Ffeed%2Fcategory%2Fsecurity%2Flatest%2Frss
https://www.wired.com/feed/category/security/latest/rss
http://feeds.feedburner.com/TechCrunch/
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
http://www.wsj.com/xml/rss/3_7031.xml
https://theintercept.com/feed/?rss
http://www.nasa.gov/rss/dyn/breaking_news.rss
https://blogs.nasa.gov/stationreport/feed/
http://www.nasa.gov/rss/dyn/mission_pages/kepler/news/kepler-newsandfeatures-RSS.rss
http://www.feedbucket.com/?src=http%3A%2F%2Fwww.nasa.gov%2Frss%2Fdyn%2Fchandra_images.rss
http://www.nasa.gov/rss/dyn/solar_system.rss
http://www.nasa.gov/rss/dyn/earth.rss
http://www.nasa.gov/rss/dyn/aeronautics.rss
http://www.esa.int/rssfeed/HSF
http://feeds.bbci.co.uk/news/science_and_environment/rss.xml?edition=uk
http://feeds.marketwatch.com/marketwatch/topstories/
http://feeds.marketwatch.com/marketwatch/marketpulse/
http://feeds.marketwatch.com/marketwatch/pf/
http://feeds.marketwatch.com/marketwatch/StockstoWatch/
http://feeds.marketwatch.com/marketwatch/internet/
http://feeds.marketwatch.com/marketwatch/mutualfunds/
http://feeds.marketwatch.com/marketwatch/financial/
https://schneier.com/blog/atom.xml
http://xkcd.com/atom.xml
http://feeds.arstechnica.com/arstechnica/index/
http://feeds.gawker.com/lifehacker/full
https://www.reddit.com/r/technology/.rss
https://www.economist.com/sections/business-finance/rss.xml
https://www.economist.com/sections/economics/rss.xml
https://www.economist.com/sections/science-technology/rss.xml
https://www.economist.com/latest-updates
https://www.economist.com/sections/united-states/rss.xml
https://www.economist.com/sections/china/rss.xml
https://www.economist.com/sections/americas/rss.xml
https://www.economist.com/sections/international/rss.xml
https://www.economist.com/sections/europe/rss.xml
https://www.economist.com/sections/asia/rss.xml
"""

categories, txt_categories, dict_categories = [], [], {}

# def addCategory(name, criteria):
#     global categories, txt_categories, dict_categories
#     categories.append(criteria); txt_categories.append(name)
#     dict_categories[name] = criteria

#OVERRIDES addCategory to update criteria without adding new targetable sections
def addCategory(name, criteria):
    global categories, txt_categories, dict_categories
    if name in txt_categories:
        for ndx in range(len(txt_categories)):
            if name == txt_categories[ndx]:
                categories[ndx] = criteria
    else:
        categories.append(criteria);
        txt_categories.append(name)
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

business = """
25: money
20: economy
25: stock-market
25: stocks
25: stockmarket
10: wealth
25: savings
40: gold
35: real estate
30: finance
40: saving
20: business
"""
addCategory('Business', business)

usa_politics = """
30: politics
60: gerrymandering
55: midterms
25: election
30: united states politics
30: republican
30: democrat
20: Federal Government
15: Legislature
15: Executive
15: Judiciary
15: Elections
15: Political parties
15: Federalism
15: liberals
15: conservatives
15: progressives
15: libertarian
15: constitution
10: congress
10: house of representatives
10: speaker of the house
10: senate majority leader
"""
addCategory('USA politics', usa_politics)

asia = """
40: china
50: china trade
40: china economy
45: asian economy
35: south china sea
20: Malaysia
20: Singapore
30: South Korea
15: Sri Lanka
20: Taiwan
20: Thailand
15: Vietnam
15: Philippines
15: Laos
10: Bangladesh
25: Bhutan
20: Cambodia
35: India
30: Indonesia
40: japan
"""
addCategory('Asia', asia)

europe = """
35: europe
20: eu
20: brexit
25: germany
30: spain
25: migrants
"""
addCategory('Europe', europe)

college = """
10: college, school
30: university|college,rankings
30: college,tuition
35: best degrees
20: best paying degrees
"""
addCategory('University', college)

health = """
30: healthy life
35: healthy life style
20: dieting
35: fitness
25: bodybuilding
15: athlete
"""
addCategory('Health', health)

law = """
10: congress
25: bills, -dolla dolla
20: new law
15: judge
25: federal judge(|s)
20: judge appointment(|s)
"""
addCategory('Law', law)

food = """
30: food
30: meal recipes
25: budget recipes
20: recipes
"""
addCategory('Food', food)

travel = """
35: travel(|ing)
50: cheap flight(|s)
45: travel adventure(|s)
40: budget traveling(|ing)
25: summer activities(y|ies)
25: winter activities(y|ies)
25: fall activities(y|ies)
25:spring activities(y|ies)
45: travel idea(|s)
45: how to travel
45: travel guide(|s)
"""
addCategory('Travel', travel)

music = """
20: (best|top|great) song(|s)
15: (best|great) album(|s)
20: concert(|s), music concert(|s)
"""
addCategory('Music', music)

entertainment = """
20: movie
30: new movie
35: (best|good|great) (show|movie)
10: new tv shows
"""
addCategory('Entertainment', entertainment)

crypto = """
20: cryptocurrenc(y|ies)
10: bitcoin(|s)
15: alt( |-)coins"""
addCategory('Crypto', crypto)

space_stuff = """
65: NASA
25: astronomy, -gastronomy
25: MIT
500: faster than light
500: faster-than-light
500: wormholes
500: space travel
250: space colonization
75: space, space travel
55: faster then light travel
65: mars colonization
15: aliens
30: wormholes
20: planets
"""
addCategory('Space', space_stuff)

climate = """
15: climate change
15: carbon
40: air pollution
15: toxic
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

xkcd = "1000: xkcd"
addCategory('xkcd', xkcd)

entries, named_categories = [], list(dict_categories.keys())
