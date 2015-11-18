import csv
import sys
import random
import string
from datetime import date

fin = open('klanten.csv', 'rt')
fout = open('klanten_nieuw.csv', 'wt')
try:
	reader = csv.reader(fin)
	writer = csv.writer(fout)
	klantnr = 0
	for row in reader:
		if (row[0] == 'Naam'):
			row.append('Leeftijd')
			row.append('Password')
			row.append('Klantnummer')
			row.append('Username')
		else:
			row.append(date.today().year - int(row[1]))
			row.append(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)))
			row.append(klantnr)
			klantnr += 1
			row.append(row[0] + row[1])
		print(row)
		writer.writerow(row)
finally:
	fin.close()
	fout.close()