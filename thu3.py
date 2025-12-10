import json

with open('students.json','r',encoding='utf-8') as filejson:
    noidung = json.load(filejson)

sinhvien = noidung['students']
for i in sinhvien:
    print(i)