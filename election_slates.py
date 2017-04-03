# Usage: simply fill in noms and key

from __future__ import print_function, division

labels = ['Pres', '1VP', '2VP', 'CorSec', 'RecSec', 'Treas', 'S@A']

noms = [
    # President
    {'hfernand', 'dtv', 'dhreed', 'jpdoyle', 'asilverg'},
    # 1VP
    {'jpdoyle', 'hfernand', 'dtv', 'kfair', 'igriswol', 'mhthomps',
        'asilverg'},
    # 2VP
    {'hfernand', 'igriswol', 'nrauen', 'asilverg'},
    # CorSec
    {'hhausman', 'mrquinn', 'mforsman', 'mhthomps', 'asilverg', 'hfernand'},
    # RecSec
    {'dhreed', 'igriswol', 'hhausman', 'mhthomps', 'nrauen', 'axe', 'asilverg',
        'hfernand'},
    # Treasurer
    {'jpdoyle', 'cjwong', 'asilverg', 'jagu', 'hhausman'},
    # S@A
    {'nrauen', 'cjwong', 'ekrakopo', 'dhreed', 'kthies', 'asilverg',
        'hhausman', 'hfernand'}
]

# Due to tabs, names need to be less than 7 letters
key = {
    'asilverg': 'Asher',
    'axe': 'Alka',
    'cjwong': 'Cam',
    'dhreed': 'Dez',
    'dtv': 'Dylan',
    'ekrakopo': 'Kate',
    'hfernand': 'Harry',
    'hhausman': 'Henry',
    'igriswol': 'Ian',
    'jagu': 'Joy',
    'jpdoyle': 'Joe',
    'kfair': 'Rin',
    'kthies': 'Kevin',
    'mforsman': 'Mady',
    'mhthomps': 'Matt',
    'mrquinn': 'Quinn',
    'nrauen': 'Rauen',
}

empty = '______'

def remove(noms, person):
  return [nom - {person} for nom in noms]

def slates(noms):
  if len(noms) == 0:
    return [[]]
  else:
    pos = noms[0]
    if len(pos) == 0:
      pos = [empty]
    rem = noms[1:]
    return [[p] + r for p in pos for r in slates(remove(rem, p))]

def print_slates(slates):
  for l in labels:
    print(l, '\t', end='')
  print('\n=======================================================')
  for slate in slates:
    for p in slate:
      print(p, '\t', end='')
    print('')

results = [[key[p] if p in key else p for p in slate] for slate in slates(noms)]
good_slates = [slate for slate in results if empty not in slate]
bad_slates = [slate for slate in results if empty in slate]

print_slates(good_slates)
print(len(good_slates), 'full slates.')

if len(bad_slates) == 0:
  print('No potential empty positions!')
else:
  print('')
  print('WARNING: Potentially empty slates:')
  print_slates(bad_slates)
  print(len(bad_slates), 'slates with empty positions.')

