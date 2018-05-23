import csv
import re

dict = {}
with open('autolib.csv') as csvfile:
  reader = csv.reader(csvfile, delimiter=';')
  #reader = csv.DictReader...
  for line in reader: 
    #if row['Postal code'][:3] == '750'
    if re.match('^(750)[0-9]{2}$', line[12]):
      if line[12] in dict:
        dict[line[12]] += int(line[1])
      else:
        dict.update({line[12]: int(line[1])})
  print dict


