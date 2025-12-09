from datetime import datetime

def time(s):
    return datetime.strptime(s, "%d/%m/%Y")

class Phim:
    def __init__(self, i, ma, loai, date, ten, tap):
        self.stt = f'P{i:03d}'
        self.ma = ma
        self.ten = ten
        self.loai = loai
        self.date = date
        self.tap = tap
        self.tg = time(date)

    def __str__(self):
        return f'{self.stt} {self.loai} {self.date} {self.ten} {self.tap}'

if __name__ == '__main__':
    n, m = map(int, input().split())
    list_phim = []
    for i in range(n):
        list_phim.append(input())
    ds = []
    for i in range(1, m + 1):
        ma = input().strip()
        date = input().strip()
        ten = input().strip()
        tap = int(input())
        loai = list_phim[int(ma[-3:])-1]
        ds.append(Phim(i, ma, loai, date, ten ,tap))

    ds.sort(key=lambda x : (x.tg, x.ten, -x.tap))

    for x in ds:
        print(x)

