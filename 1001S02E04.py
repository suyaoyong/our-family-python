print("正常版")
for a in range(1,10):
    for e in range(1,a+1):
        c = (a*e)
        if e == a:
            print(a,"*",e,"=",c,end='\n')
        elif e < a:
            print(a,"*",e,"=",c,end='\t')
       
print("没有偶数版（厉害吧，不用while语句哦）")
for a in range(1,10,2):
    for e in range(1,10):
        c = (a*e)
        if e == a:
            print(a,"*",e,"=",c,end='\n')
        elif e < a:
            print(a,"*",e,"=",c,end='\t')