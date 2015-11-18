import matplotlib.pyplot as plt
import csv
f = open('data.csv', 'rt')

labels = []

try:
	reader = csv.reader(f)
	for row in reader:
		if (row[0] == 'Date'):
			print("Header!")
			print(row[1])
		else:
			for i in row[1:3]:
				print(i)
			pass
finally:
	f.close()