#Converts the geo_data tvs into a more ArcMap friendly csv
import csv
import sys

fin = open('geo_data.tsv', 'r')
fout = open('geo_data.csv', 'w')

csv.field_size_limit(sys.maxsize)

tabfile = csv.reader(fin, dialect=csv.excel_tab)
commafile = csv.writer(fout, dialect=csv.excel)
 
for row in tabfile:
        commafile.writerow(row) 

print "done"
