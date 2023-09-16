import csv

dataset1 = []
dataset2 = []


with open('final.csv', 'r') as o:
    dataset1.append(o)


with open('dataset1.csv', 'r') as o:
    dataset2.append(o)
 
header1 = dataset1[0]
header2 = dataset2[0]

planetdata1 = dataset1[1:]
planetdata2 = dataset2[1:]

planetdata = []
for index, datarow in enumerate(planetdata1):
    planetdata.append(planetdata1[index] + planetdata2[index])

headers = (header1) + (header2)

with open('dataset5.csv', 'a+') as o:
    csvwriter = csv.writer(o)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)


