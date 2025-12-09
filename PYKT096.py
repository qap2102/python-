class Doi:
    def __init__(self, i, ten_team, truong)->None:
        self.ma = f'{str(i).zfill(2)}' 
        self.ten_team = ten_team
        self.truong = truong
        
    def __str__(self):
        return f'{self.ma} {self.ten_team} {self.truong}'
    

class ThiSinh:
    def __init__(self, i, ten_team, truong, ten, mateam)->None:
        
        self.ten_team = ten_team 
        self.truong = truong     

        self.ma_ts = f'C{str(i).zfill(3)}' 
        self.ten = ten
        self.mateam = mateam 
    
    def __str__(self):
 
        return f'{self.ma_ts} {self.ten} {self.ten_team} {self.truong}'

d = {} 

so_team = int(input()) 

    
for i in range(so_team):
    ten_team = input() 
    truong = input()   
    doi = Doi(i + 1, ten_team, truong)
    d[doi.ma] = doi 

b = []

n = int(input()) 

    
for i in range(n):
    ten = input()   
    mateam = input()

    tmp = mateam[-2:]

    if tmp in d.keys():
        doi_info = d[tmp]

        b.append(ThiSinh(i + 1, doi_info.ten_team, doi_info.truong, ten, mateam))
    
b.sort(key=lambda x: x.ten)
for ts in b:
    print(ts)