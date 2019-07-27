text1 = '''
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

def stats_text_en(n) :          #统计参数中每个英文单词出现的次数，最后返回一个按字频降序排列的数组
    n = n.replace(',','')
    n = n.replace('.','')
    n = n.replace('!','')
    n = n.replace('--','')
    n = n.replace('*','')
    n = n.replace("'",'')

    n = n.split()
    list_n = list(n)

    dict_n = {}
    for i in list_n:
        dict_n[i] = list_n.count(i)

    d = sorted(dict_n.items(), key=lambda x: x[1],reverse =True )
    #d.reverse()
    print(d)

stats_text_en(text1)


text2 = '''
定义是一个汉语词语，原指对事物做出的明确价值描述。
现代定义：对于一种事物的本质特征或一个概念的内涵和外延的确切而简要的说明；
或是透过列出一个事件或者一个物件的基本属性来描述或规范一个词或一个概念的意义。
被定义的事件或者物件叫做被定义项。
一般地，能清楚的规定某一名称或术语的概念叫做该名称或术语的定义。
对于一种事物的本质特征或一个概念的内涵和外延所作的简要说明。
相当于数学上的对未知数的设定赋值，比如“设某未知数为已知字母x以便于简化计算，”对某个命名的词汇赋与一定的意义或形象，则有利于交流中的识别及认同。
命名和定义总是相伴而生，用已知的熟知的来解释和形容未知的陌生的事物并加以区别，这是一个理论界的真理。
值得注意的是定义是一种表述并非自主认知来源，过度拘泥于它会扼杀知道但无法表述的事物。
简单来说，定义是一种人为的广泛、通用的解释意义，如人名（绰号、姓名）、符号、成语…等等
'''

def stats_text_cn(a) :       #统计参数中每个中文汉字出现的次数，最后返回一个按字频降序排列的数组
    a = str(a)
    word_list = []
    word_dict = {}
    exclude_str = '''，。！？、（）【】<>《》=：+-*—“”…'''

    for word in a:
        word_list.append(word)
    for word in word_list :
        if word not in exclude_str :
            if word.strip() not in word_dict :
                word_dict[word] = 1
            else :
                word_dict[word] += 1

    word_out = sorted(word_dict.items(), key=lambda x: x[1],reverse =True )
    print(word_out)
#x[1]是按字频排序，x[0]是按字排序

stats_text_cn(text2)