

class Computation:
    def __init__(self, n: int) -> None:
        self.n = n

    def Factorial(self, k: int = None) -> int:
        if k is None:
            k = self.n

        if k < 0:
            return 0 

        if k == 0:
            return 1

        return k * self.Factorial(k - 1)


    def Prime(self, k: int = None) -> str:
        if k is None:
            k = self.n

        if k < 2:
            return 'NO'
            

        for i in range(2, int(k**0.5) + 1):
            if k % i == 0:
                return 'NO'
        
        return 'YES'


    def listDiv(self, k: int = None) -> list:
        if k is None:
            k = self.n
            
        if k <= 0:
            return []
        
        uoc_so_nho = []
        uoc_so_lon = []
        
        i = 1
        while i * i <= k:
            if n % i == 0:

                uoc_so_nho.append(i)

                uoc_lon = k // i

                if uoc_lon != i:
                    uoc_so_lon.append(uoc_lon)
                    
            i += 1
        return uoc_so_nho + uoc_so_lon[::-1]

n=int(input())
a = Computation(n)

print(a.Factorial())
print(a.Prime())

for i in a.listDiv():
    print(i, end=',')