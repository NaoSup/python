# MAP
def minusThree(nb):
  return nb - 3

myList = (6, 3, 8, 4, 2)

def myMap( myList ):
  for i in myList:
    yield minusThree(i)

# print(list(minusList(myList)))

# print(map(minusThree, myList)) 

# print(map(lambda x: x - 3, myList))



# FILTER
myTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
myList2 = []

def isEven( nb ):
  return nb % 2 == 0

def keepEven( tup ):
  for i in tup:
    if isEven(i):
      yield i

for i in myTuple:
  if i % 2 == 0:
    myList2.append(i)

# print(list(keepEven(myTuple)))

# print(list(filter(isEven, myTuple)))

# print(list(filter(lambda x: x % 2 == 0, myTuple)))

# GROUPBY
maListe = (("a", 3), ("b", 2), ("a", 4), ("a", 9), ("c", 1))

groupName = ""
myRes = []

from itertools import groupby

for el in maListe:
  if(el[0] != groupName):
    groupName = el[0]
    myRes.append([groupName, [el]])
  else:
    myRes[len(myRes) - 1][1].append(el)

# print(list(myRes))
# print(list(map(lambda x: (x[0], list(x[1])), groupby(maListe, lambda x: x[0]))))

# REDUCE
from functools import reduce

tup = (1, 2, 3, 4)

print(reduce(lambda a, x: a + x, tup))

res = 0
for i in tup:
  res += i
print(res)


