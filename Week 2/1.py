import csv
f = open('klanten.csv', 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        print(row[0], row[2])
finally:
    f.close()