import string

def chuanhoa(s):
    return string.capwords(s)

def PhanLoai(s):
    if s=='A':
        return 100
    elif s=='B':
        return 500
    else:
        return 200

class KhachHang:
    def __init__(self, i, ten, loai, dau, cuoi)->None:
        self.ma = f'KH{str(i).zfill(2)}'
        self.ten = chuanhoa(ten)
        self.loai = loai
        self.dau=dau
        self.cuoi=cuoi
    def trong(self)->int:
        sodien = self.cuoi-self.dau
        pl = PhanLoai(self.loai)
        if sodien < pl:
            return sodien*450
        else:
            return pl*450
        
    def vuot(self)->int:
        sodien = self.cuoi-self.dau
        pl = PhanLoai(self.loai)
        if sodien>pl:
            return (sodien-pl)*1000
        else:
            return 0
        
    def vat(self)->int:
        return self.vuot()//20
    
    def tong(self)->int:
        return self.trong()+self.vuot()+self.vat()
    
    def __str__(self):
        return f'{self.ma} {self.ten} {self.trong()} {self.vuot()} {self.vat()} {self.tong()}'
    

a=[]
n=int(input())
for i in range(n):
    ten = input()
    tmp = input()
    b = tmp.split()
    loai = b[0]
    dau = int(b[1])
    cuoi = int(b[2])
    a.append(KhachHang(i+1,ten,loai,dau,cuoi))

a.sort(key= lambda x: -x.tong())

for i in a:
    print(i)
    