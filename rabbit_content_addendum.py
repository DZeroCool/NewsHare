#USE from rabbit_content_addendum import *
global feeds

feeds +=  """\n
https://schneier.com/blog/atom.xml
http://xkcd.com/atom.xml
http://feeds.arstechnica.com/arstechnica/index/
http://feeds.gawker.com/lifehacker/full
https://www.reddit.com/r/technology/.rss
"""

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

tech += """\n20: feds 
25: trade
"""
addCategory('Technology', tech)

business += """\n
25: money
20: economy
"""
addCategory('Business', business)

usa_politics += """\n
30: politics
"""
addCategory('USA politics', usa_politics)

asia += """\n
50: china
20: china, trade
20: china, economy
40: asian economy
40: military, south china sea
"""
addCategory('Asia', asia)

europe = """\n
35: europe
20: EU,eu
"""
addCategory('Europe', europe)

college += """\n
10: college, school
30: university|college,rankings
30: college,tuition
"""
addCategory('University', college)

health += """\n
30: healthy, life
10: healthy, lifetyle
30: dieting
25: exercise
30: exercising
30: fitness
10: health, body
"""
addCategory('Health', health)

law = """\n
25: congress
25: bills,-dolla dolla
35: new law
10: judge
30: federal judges
35: judge appointments
"""
addCategory('Law', law)

food += """\n
30: food
20: meal recipe
20: budget recipe
20: recipes
"""
addCategory('Food', food)

travel += """\n
40: travel
40: cheap flights
50: travel adventures
50: budget traveling
30: recreation
20: summer activities
20: winter activities
20: fall activities
20: spring activities
45: travel ideas
45: how to travel
45: travel guides
"""
addCategory('Travel', travel)

music += """\n
20: top songs
15: best albums
20: concerts, music concerts
"""
addCategory('Music', music)

entertainment += """\n
20: movie
30: new movie
35: (best|good|great show|movie)
"""
addCategory('Entertainment', entertainment)

crypto += """\n
20: cryptocurrenc(y|ies)
10: bitcoin(|s)
15: alt( |-)coins"""
addCategory('Crypto', crypto)

space_stuff += """\n
"""
addCategory('Space', space_stuff)

climate += """\n
40: air pollution, toxic
"""
addCategory('Climate', climate)

world_affairs += """\n
35: sanctions
"""
addCategory('World Affairs', world_affairs)

entries, named_categories = [], list(dict_categories.keys())
