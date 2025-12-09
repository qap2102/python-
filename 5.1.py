def kt_mat_khau_chuan(s):
    if len(s) < 6 or len(s) > 12:
        return False

    
    kt1 = False
    kt2 = False
    kt3 = False
    kt4 = False
    
    ky_tu_dac_biet = '$#@!' 

    for ky_tu in s:
        if ky_tu.islower():
            kt1 = True
        elif ky_tu.isupper():
            kt2 = True
        elif ky_tu.isdigit():
            kt3 = True
        elif ky_tu in ky_tu_dac_biet:
            kt4 = True
        
        
        if kt1 and kt2 and kt3 and kt4:
            break

    
    if kt1 and kt2 and kt3 and kt4:
        return True
    else:
        return False

a=list(map(str, input().split(',')))

kt=False
cnt=0
b=[]

for i in a:
    if kt_mat_khau_chuan(i):
        b.append(i)

if len(b)==0:
    print('INVALID PASSWORD')
elif len(b)==1:
    for i in b:
        print(i)
else:
    for i in b:
        print(i, end=',')

