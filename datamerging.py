import csv
import pandas as pd

file1="bright_stars.csv"
file2="dwarf_stars.csv"

d1=[]
d2=[]

with open(file1,"r",encoding="utf8")as f:
    csv_reader=csv.reader(f)
    for i in csv_reader:
        d1.append(i)

with open(file2,"r",encoding="utf8")as f:
    csv_reader=csv.reader(f)
    for i in csv_reader:
        d2.append(i)      

h1=d1[0]
h2=d2[0]

r1=d1[1:]
r2=d2[1:]

h=h1+h2

r3=[]
for i in r1:
    r3.append(i)
for j in r2:
    r3.append(j)

with open ("new_stars.csv","w",encoding="utf8")as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(h)
    csv_writer.writerows(r3)

df=pd.read_csv("new_stars.csv")


