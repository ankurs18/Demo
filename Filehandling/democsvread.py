import csv

fobj=open('C:\\python\\data.csv')

fdata=csv.reader(fobj)
mylist =list(fdata)
print(mylist)

