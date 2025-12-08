t=int(input())
for _ in range(t):
    s=input()
    d={}
    for i in s:
        d[i] = d.get(i,0)+1
    
    tmp = max(d.values())

    for i,j in d.items():
        if j == tmp:
            print(i)
            break