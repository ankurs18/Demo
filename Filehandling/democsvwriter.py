import csv
#a for append
wobj=open('C:\\python\\new.csv', 'w', newline='')

wr=csv.writer(wobj)
wr.writerow(['id','name','age'])
wr.writerow(['101','ankur','23'])
wr.writerow(['102','sethi','232'])

wobj.close()