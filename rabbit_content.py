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
"""

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
