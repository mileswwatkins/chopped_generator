# -*- coding: utf-8 -*-
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
    text = ingredients.text_content()
    (course, items) = text.split(':')
    items = [x.strip() for x in items.split(',')]
    if course == "Appetizer":
        appetizers.extend(items)
    elif course == u"Entrée":
        entrees.extend(items)
    elif course == "Dessert":
        desserts.extend(items)
    else:
        raise AssertionError("Unidentified course found")

print(u"Appetizer round: {}".format(', '.join(random.sample(appetizers, 4))))
print(u"Entrée round: {}".format(', '.join(random.sample(entrees, 4))))
print(u"Dessert round: {}".format(', '.join(random.sample(desserts, 4))))
