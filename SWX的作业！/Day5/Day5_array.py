a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("第2小题")
a.reverse()
print(a)

print("第3小题")
b = [str(i) for i in a]   #要把a里面的整形全部变成字符串才行啊
s = ''.join(b)
print(s)

print("第4小题")
s2 = s[2:8]
print(s2)

print("第5小题")
s2 = s2[::-1]
print(s2)

print("第6小题")
s2 = int(s2)
print(s2)

print("第7、8小题")
print("二进制：",bin(s2).replace('0b',''))
print("八进制：",oct(s2).replace('0o',''))
print("十六进制：",hex(s2).replace('0x',''))