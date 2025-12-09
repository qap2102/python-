import string

def chuanhoa(s):
    return string.capwords(s)

class ThiSinh:
    def __init__(self, i, ten, diem, dantoc, kv) -> None:
        self.ma = f'TS{str(i).zfill(2)}'
        self.ten = chuanhoa(ten)
        self.dantoc = dantoc

        self.kv = int(kv) 
        
        self.diem = diem + self.TongDiem()

        if self.diem >= 20.5: 
            self.tt = 'Do'
        else: 
            self.tt = 'Truot'
            
    def TongDiem(self) -> float:
        tmp = 0.0 
        if self.dantoc != 'Kinh':
            tmp += 1.5
        if self.kv == 1:
            tmp += 1.5
        elif self.kv == 2:
            tmp += 1.0
        return tmp
    
    def pri(self):
        return f'{self.ma} {self.ten} {self.diem:.1f} {self.tt}'
        
    def __str__(self):
        return self.pri()

a = []
n = int(input())

for i in range(n):
    ten = input()
    diem = float(input())
    dantoc = input()
    kv = input() 

    a.append(ThiSinh(i + 1, ten, diem, dantoc, kv))

a.sort(key=lambda x: -x.diem)

for ts in a:
    print(ts)