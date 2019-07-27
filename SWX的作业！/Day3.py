p = input("第一个数")
b = input("第二个数")

p = float(p)
b = float(b)

sym=input("运算方式")

if sym == "+":
    result=p+b
if sym == "-":
    result=(p-b)
if sym == "*":
    result=(p*b)
if sym == "/":
    result=(p/b)
print(result)