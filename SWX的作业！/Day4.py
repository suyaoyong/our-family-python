print("正常版")
for a in range(1,10):
    for e in range(1,a+1):
        c = (a*e)
        if e == a:
            print(a,"*",e,"=",c,end='\n')
        elif e < a:
            print(a,"*",e,"=",c,end='\t')
       
print("没有偶数版")
a = 1
while a < 10:
    b = 1
    while a % 2 != 0 and b <= a:
        #if e == a :
        print(a,"*",b,"=",a*b,end='\t')
        #elif e < a:
        #print(a,"*",b,"=",c,end='\t')       
        b += 1
    
    else:
        a += 1
    print ()
        
        