# Usage: simply fill in noms

from __future__ import print_function, division

labels = ['Pres', '1VP', '2VP', 'CorSec', 'RecSec', 'Treas', 'S@A']

noms = [
    # President
    {'djyin', 'bennerr'},
    # 1VP
    {'djyin', 'bennerr', 'eplin'},
    # 2VP
    {'eplin', 'ngaynor'},
    # CorSec
    {'djyin', 'ngaynor', 'bennerr', 'evj', 'eplin', 'isaacw'},
    # RecSec
    {'djyin', 'ngaynor', 'jholz', 'bennerr'},
    # Treasurer
    {'djyin', 'bennerr', 'jholz', 'ngaynor', 'eplin', 'noahking'},
    # S@A
    {'bennerr', 'djyin', 'ngaynor', 'jholz', 'vsaige', 'eplin', 'noahking', 'isaacw'}
]

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

def candidates(noms):
  candidates = set()
  for pos in noms:
    candidates |= pos
  return candidates

def print_slates(slates, tab):
  for l in labels:
    print(l.ljust(tab), end='')
  print('\n' + '='*7*tab)
  for slate in slates:
    for p in slate:
      print(p.ljust(tab), end='')
    print('')

tab = len(max(candidates(noms), key=len)) + 2
empty = '_'*(tab-4)

results = [[p for p in slate] for slate in slates(noms)]
good_slates = [slate for slate in results if empty not in slate]
bad_slates = [slate for slate in results if empty in slate]

print_slates(good_slates, tab)
print(len(good_slates), 'full slates.')

if len(bad_slates) == 0:
  print('No potential empty positions!')
else:
  print('')
  print('WARNING: Potentially empty slates:')
  print_slates(bad_slates, tab)
  print(len(bad_slates), 'slates with empty positions.')

