# -*- coding: utf-8 -*-

import codecs
import csv

# maliste = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
monDict = {}

with codecs.open( './autolib.csv', 'rU', encoding = "utf-8", errors = "ignore" ) as csvfile:
    reader = csv.DictReader( csvfile, delimiter=';' )

    for row in reader:
        codepostal = row[ 'Postal code' ]
        if codepostal[:3] == "750":

            if not codepostal in monDict:
                monDict[ codepostal ] = 0

            monDict[ codepostal ] += int( row[ 'Cars' ] )
            # maliste[ int( codepostal[ 3: ] ) - 1 ] += int( row[ 'Cars' ] )
            
print( monDict )
# print( maliste )