import math
class PhanSo:
    def __init__(self, tu, mau)-> None:
        self.tu=tu
        self.mau=mau
    def RutGon(self, a, b)-> str:
        self.tu = a//math.gcd(a,b)
        self.mau = b//math.gcd(a,b)

        return f'{self.tu}/{self.mau}'

a=list(map(int,input().split()))

b = PhanSo(a[0],a[1])

print(b.RutGon(a[0],a[1]))