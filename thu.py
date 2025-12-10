with open('A.txt') as A:
    with open('B.txt') as B:
        for x,y in zip(A.readlines(),B.readlines()):
            try:

                print(int(x)**int(y))
            except:
                print("INVALID")