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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
sym = ",.*!-"
for i in sym:
    text = text.replace(i,"")
print(text)
list1 = text.split()
#print(list1)
set1 = set(list1)
dic1 = {}
for word in set1:
    dic1[word] = list1.count(word)
#print(dic1)
print("print the words",sorted(dic1.items(), key=lambda x:x[1],reverse = True))
#dic2 = sorted(dic1.items(), key=lambada x:x[1],reverse = True)
#print(dic2)