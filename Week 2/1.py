import csv
csv.register_dialect('puntcomma', delimiter=';')
f = open('klanten.csv', 'rt')
try:
    reader = csv.reader(f, dialect='puntcomma')
    for row in reader:
        print(row[0], row[2])
finally:
    f.close()

