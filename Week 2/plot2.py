import matplotlib.pyplot as plt
import csv
import numpy

f = open('data.csv', 'rt')
xas = []
top1 = []
top2 = []
top3 = []
top4 = []
top5 = []
top6 = []
top7 = []
labels = []

try:
    reader = csv.reader(f)
    for row in reader:
    	if (row[0] == 'Date'):
    		print("Header!")
    		labels.append(row[1])
    		labels.append(row[2])
    		labels.append(row[3])
    		labels.append(row[4])
    		labels.append(row[5])
    		labels.append(row[6])
    		labels.append(row[7])
    	else:
	        xas.append(row[0])
	        top1.append(row[1])
	        top2.append(row[2])
	        top3.append(row[3])
	        top4.append(row[4])
	        top5.append(row[5])
	        top6.append(row[6])
	        top7.append(row[7])
finally:
    f.close()
print('xas', xas)
print('labels', labels)
print('top1', top1)
plt.plot(xas,top1,xas,top2,xas,top3,xas,top4,xas,top5,xas,top6,xas,top7)
plt.ticklabel_format(useOffset=False)
plt.xticks(range(2011,2015))
plt.title('Top 7 Desktop OS\'en')
plt.xlabel('Jaar')
plt.ylabel('Populariteit (%)')
plt.grid(True)
plt.legend(labels,loc='best')
plt.show()