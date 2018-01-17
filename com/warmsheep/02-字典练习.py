#写代码，有如下字典，按要求实现每一个功能，dic={'k1':'v1','k2':'v2','k3':'v3'}
#1.请循环遍历出所有的 key
#方法1：
dic={'k1':'v1','k2':'v2','k3':'v3'}
for key in dic.keys():
    print(key)

# #方法2：
dic={'k1':'v1','k2':'v2','k3':'v3'}
for key in dic:
    print(key)

#方法3
for k,v in dic.items():
    print(k)



#2.请循环遍历出所有的 value
#方法1：
for v in dic.values():
    print(v)

#方法2：
for k,v in dic.items():
    print(v)



#3.请循环遍历出所有的 key 和 value
for k,v in dic.items():
    print(k,v)
#k1 v1
# k2 v2
# k3 v3



#4.请在字典中添加一个键值对，'k4':'v4'，输出添加后的字典
#方法1：dict.update(dict2)
dic.update({'k4':'v4'})
print(dic)
#{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}

#方法2：dict[key]=value
dic["k4"] ="v4"
print(dic)
#{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}



#5.请删除字典中键值对'k1':'v1'，并输出删除后的字典
#方法1：del dict(key)
del dic["k1"]
print(dic)
#{'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}

#方法2：dict.pop(key）
dic.pop("k1")
print(dic)
{'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}



#6.请删除字典中的键'k5'对应的键值对，如果字典不存在键'k5'，则不报错，并且让其返回 None
#方法1：用dic.get(key[,defalut=None])
dic={'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
dic.get("k5")
print(dic.get("k5","None")) #None
print(dic) #{'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}

#方法2：用dic.get(key[,defalut=None])
# None可以省略，其实默认就返回None
dic={'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
dic.get("k5")
print(dic.get("k5")) #None



#7.请获取字典中'k2'对应的值
dic.get("k2")
print(dic.get("k2")) #v2



#8.请获取字典中'k6'对应的值，如果字典不存在键'k6'，则不报错，并且让其返回 None
#方法1：用dic.get(key[,defalut=None])
dic={'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
dic.get("k6")
print(dic.get("k6","None")) #None
print(dic) #{'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}

#方法2:用dic.get(key[,defalut=None])
# None可以省略，其实默认就返回None
dic={'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
dic.get("k6")
print(dic.get("k6")) #None



#9.现有 dic2={'k1':'v111','a':'b'}通过一行操作使dic2={'k1':'v1','k2':'v2','k3':'v3','a':'b'}
#用dict.update(dict2)
dic2={'k1':'v111','a':'b'}
dic2.update({'k1':'v1','k2':'v2','k3':'v3'}) #将k1的值更新，并新增k2和k3键值对
print(dic2) #{'k1': 'v1', 'a': 'b', 'k2': 'v2', 'k3': 'v3'}字典中是无序的，所以显示虽然和答案不同，但是其实是一样的



#10.组合嵌套题。
    #list=[['k':['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
    #1.将列表list中的'tt'变成大写(用两种方式)

#方法1：
list=[['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
list[0][1][2]={'k1':['TT',3,'1']}
# print(list)
list[0][1][2].values()
print(list[0][1][2].values())

#方法2：
s=list[0][1][2].get("k1")
print(s) #['tt', 3, '1']
s[s.index("tt")]=s[s.index("tt")].upper()
print(list)


#2.将列表中的数字3变成字符串'100'（用两种方式)
#方法1
list[0][1][2]={'k1':['tt',100,'1']}
print(list)

#方法2
s=list[0][1][2].get("k1")
print(s) #['tt', 3, '1']
s[s.index(3)]=100
print(list)


#3.将列表中的字符串'1'变成数字101（用两种方式)
#方法1
list[0][1][2]={'k1':['tt',3,'101']}
print(list)

#方法2
s=list[0][1][2].get("k1")
print(s) #['tt', 3, '1']
s[s.index('1')]=101
print(list)




#11.按照要求实现以下功能
    #现有一个列表 li=[1,2,3,'a','b',4,'c'],有一个字典（此字典是动态生成的，你并不知道他里面有多少键值对，所以用dic={}模拟此字典），现需要完成以下操作：
    #如果该字典没有'k1'这个键，那就创建这个'k1'这个键和其对应的值（该键对应的值设置为空列表），并将列表li中的索引位为奇数对应的元素，添加到'k1'这个键对应的空列表中。
    #如果该字典有'k1'这个键，且k1对应的value 是列表类型，那就将列表 li 中的索引位为奇数对应的元素，添加到'k1'这个键对应的值中

#我的解法（老师说比较节省时间，具体的，emmmm.....我还没学到那里）
li = [1, 2, 3, 'a', 'b', 4, 'c']
dic = {"k1": 12}
list1 = []
list2 = []
if dic.get("k1") == None:  # 判断"k1"是否在字典里
    print("k1键不存在")
    for i in range(len(li)): #range(len(li））为li的所有索引值
    # for i,v in enumerate(li)
        if i % 2 == 1:
            list1.append(li[i])
            dic2 = {"k1": list1}
            dic.update(dic2)
            print(dic)
else:
    print("k1键已经存在")
    if isinstance(dic.get("k1"), list):
        for i in range(len(li)):
            if i % 2 == 0:
                list1.append(li[i])
                dic3 = {"k1": list1}
                dic.update(dic3)
                print(dic)
    else:
        print("k1键所对应的值为:", dic.get("k1"))
