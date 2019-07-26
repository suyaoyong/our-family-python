text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly. 
Explicit is better than implicit. 
Simple is better than complex.
Complex is better than complicated. 
Flat is better than nested. 
Sparse is better than dense. 
Readability counts. 
Special cases aren't special enough to break the rules. 
Although practicality beats purity. 
Errors should never pass silently. 
Unless explicitly silenced. 
In the face of ambxiguity, refuse the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. 
Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea. 
Namespaces are one honking great idea -- let's do more of those!
'''
text = text.replace('better','worse')
text = text.replace(',','')
text = text.replace('.','')
text = text.replace('!','')
text = text.replace('--','')
text = text.replace('*','')
text = text.replace("'",'')

list1 = text.split()

print("第2步")
print(list1)

print("第3步")
new1 = []
for u in list1:
    if u.find('ea') >= 0:
        new1.append(u)
        #print (new1)
list1 = set(list1)
new1 = set(new1)
#list1 = list1.difference(new1)  这两种办法都只能给集合（set）使用，列表（list）就不行了
list1 -= new1
print(list1)

print("第4步")
new2 = []
for i in list1:
    #print (i)
    #print(i.swapcase())
    new2.append(i.swapcase())
print(new2)      #注意这一行的缩进，得跳出for循环才行，不然print出来的new2会有一堆，每一个print出来的new2都比上一个多一个字符串

print("第5步")
new2.sort()
print(new2)