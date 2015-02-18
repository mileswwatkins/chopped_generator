import random
import urllib2

import lxml.html


URL = 'https://en.wikipedia.org/wiki/List_of_Chopped_episodes'
html = urllib2.urlopen(URL).read()
doc = lxml.html.fromstring(html)

ingredient_lists = doc.xpath(
        '//p[text()="Ingredients:"]/following-sibling::ul[1]/li')
appetizers = []
entrees = []
desserts = []
for ingredients in ingredient_lists:
    items = ingredients.text_content()
    (course, items) = items.split(':')
    items = [x.strip() for x in items.split(',')]
    if course == "Appetizer":
        appetizers.extend(items)
    elif course == u'Entr\xe9e':
        entrees.extend(items)
    elif course == "Dessert":
        desserts.extend(items)
    else:
        raise AssertionError()

print("Appetizer round: {}".format(', '.join(random.sample(appetizers, 4))))
print("Entree round: {}".format(', '.join(random.sample(entrees, 4))))
print("Dessert round: {}".format(', '.join(random.sample(desserts, 4))))
