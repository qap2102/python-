import csv
with open('address_v2.csv',mode='r') as filecsv:
    noidung=csv.reader(filecsv)
    for i in noidung:
        print(i)