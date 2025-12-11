t=int(input())
for _ in range(t):
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    p=int(input())
    if len(v1) != len(v2):
        print("INVALID")
    else:
        n=len(v1)
        sum1=0
        for i in range(n):
            sum1 += pow(abs(v1[i]-v2[i]),p)
        minkowski = pow(sum1, 1/p)
        print(f'{minkowski:.5f}')
