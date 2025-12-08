t=int(input())
for _ in range(t):
    s=input()
    d={}

    for i in s:
        d[i]=d.get(i,0)+1

    a=[]
    b=[]
    kt=True
    kt1=True

    for i in d.keys():
        if d[i]==1:
            kt=False
            a.append(i)
        else:
            kt1=False
            b.append(i)

    if kt==True :
        print('NONE')
    else:
        print(''.join(a))
    
    if kt1==True:
        print('NONE')
    else:
        print(''.join(b))
