import csv
import sys
import random

f = open('testbestandje.csv', 'wt')
try:
	writer = csv.writer(f)
	writer.writerow( ('Nummer', 'Random nummer') )
	for i in range(100):
		writer.writerow( (i+1, random.randint(1,10000)) )
finally:
	f.close()