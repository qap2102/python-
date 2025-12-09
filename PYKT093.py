import string
import math

def chuanhoa(s):
    return string.capwords(s)

class HocSinh:
    def __init__(self, i, ten, mon1, mon2, mon3):
        self.ma = f'SV{str(i).zfill(2)}'
        self.ten = chuanhoa(ten)
        self.mon1 = mon1
        self.mon2=mon2
        self.mon3=mon3
        self.dtb = self.tb()
        self.hang = 0

    def tb(self)->float:
        return (self.mon1 * 3.0 + self.mon2 * 3.0 + self.mon3 * 2.0) / 8.0
    def __str__(self):
        return f"{self.ma} {self.ten} {(math.ceil(self.dtb*100)/100):.2f} {self.hang}"

a=[]
n = int(input())
for i in range(n):
    ten = input()
    mon1 = float(input())
    mon2 = float(input())
    mon3 = float(input())

    a.append(HocSinh(i+1,ten,mon1, mon2, mon3))

a.sort(key=lambda x: (-x.dtb, x.ma))

if a:
    a[0].hang = 1

    for i in range(1,len(a)):
        if a[i].dtb == a[i-1].dtb:
            a[i].hang = a[i-1].hang
        else:
            a[i].hang =i+1

for i in a:
    print(i)
    

