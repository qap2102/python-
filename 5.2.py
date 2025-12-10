import sys

data = sys.stdin.read().split()
n = int(data[0])
arr = list(map(int, data[1:n+1]))
k = int(data[-1])

res = [str(i) for i, v in enumerate(arr) if v == k]

if not res:
    print(-1)
elif len(res) == 1:
    print(res[0])
else:
    print(", ".join(res))
