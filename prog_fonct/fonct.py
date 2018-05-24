# -*- coding: utf-8 -*-

from itertools import groupby
from functools import reduce

# maliste = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
monDict = {}

def ReadCsvAsDict(path):
  import csv
  with open(path) as csvfile:
    return list(csv.DictReader(csvfile, delimiter=';'))

reader = ReadCsvAsDict('./autolib.csv')
filteredReader = filter(lambda x: x['Postal code'][:3] == "750", reader)
reduced = map(lambda x: (x['Postal code'], x['Cars']), filteredReader)
sortedList = sorted(reduced, key=lambda x: x[0])
groupedList = groupby(sortedList, key=lambda x: x[0])
groupedCast = list(map(lambda x: (x[0], list(x[1])), groupedList))
ListedCars = map(lambda x: (x[0], sum(list(map(lambda y: int(y[1]), x[1])))), groupedCast)
ListedCars2 = map(lambda x: (x[0], list(map(lambda y:   , x[1])))  , groupedCast)
# AvailableCars = map(lambda x: (x[0], sum(x[1])), ListedCars)

print(ListedCars2)
