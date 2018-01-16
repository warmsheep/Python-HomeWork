#1.创建一个空列表，命名为names，往里面添加old_driver,rain,jack,shanshan,peiqi,black_girl 元素
names=[] #三种方法
#方法1
names.extend(['old_driver','rain','jack','shanshan','peiqi','black_girl'])
#方法2
# names.append(['old_driver','rain','jack','shanshan','peiqi','black_girl'])
# 方法3
# names.insert(0,['old_driver','rain','jack','shanshan','peiqi','black_girl'])
print(names)


#2.往names列表里black_girl前面插入一个alex
#解答：
names.index("black_girl") #运行结果为5
names.insert(5,"alex")
print(names) #['old_driver', 'rain', 'jack', 'shanshan', 'peiqi', 'alex', 'black_girl']
#或者直接写出names.insert(names.index("black_girl"),"alex")


#3.将shanshan改为姗姗
names[names.index("shanshan")]="姗姗"
print(names) #['old_driver', 'rain', 'jack', '姗姗', 'peiqi', 'alex', 'black_girl']


#4.往names列表里rain的后面插入一个字列表，[oldboy,oldgirl]
names.insert(names.index("rain")+1,["oldboy","oldgirl"])
print(names) #['old_driver', 'rain', ['oldboy', 'oldgirl'], 'jack', '姗姗', 'peiqi', 'alex', 'black_girl']

#5.返回peiqi的索引值
names.index('peiqi')
print(names.index('peiqi')) #4


#6.创建新列[1,2,3,4,2,5,6,2],合并入names列表
list=[1,2,3,4,2,5,6,2]
names.extend(list)
print(names) #['old_driver', 'rain', 'jack', '姗姗', 'peiqi', 'alex', 'black_girl', 1, 2, 3, 4, 2, 5, 6, 2]


#7.取出names列表中索引4-7元素
#方法1：循环
l1=[]
for i in names:
    if names.index(i)>=4 and names.index(i)<=7:
     l1.append(i)
print(l1) #['姗姗', 'peiqi', 'alex', 'black_girl']

#方法2：切片
names[4:8]
print(names[4:8]) #['姗姗', 'peiqi', 'alex', 'black_girl']


#8.取出names列表中索引2:10的元素，步长为2
print(names)
#['old_driver', 'rain', ['oldboy', 'oldgirl'], 'jack', '姗姗', 'peiqi', 'alex', 'black_girl', 1, 2, 3, 4, 2, 5, 6, 2]
names[2:11:2]
print(names[2:11:2])
#[['oldboy', 'oldgirl'], '姗姗', 'alex', 1, 3]


#9.取出names列表中最后3个元素
names[-3:]
print(names[-3:]) #[5, 6, 2]


#10.循环names列表，打印每个元素的索引值和元素
#方法1
for i in range(len(names)): #对于names先取长度（元素的个数），然后再依次循环取出索引值和元素
#range()函数内只有一个参数，则表示会产生从0开始计数的整数列表
    print(i,names[i])
#0 old_driver
# 1 rain
# 2 ['oldboy', 'oldgirl']
# 3 jack
# 4 姗姗
# 5 peiqi
# 6 alex
# 7 black_girl
# 8 1
# 9 2
# 10 3
# 11 4
# 12 2
# 13 5
# 14 6
# 15 2

#方法2：
for index,item in enumerate(names):#enumerate函数，index，item分别代表索引值和元素
    print(index,item)
#0 old_driver
# 1 rain
# 2 ['oldboy', 'oldgirl']
# 3 jack
# 4 姗姗
# 5 peiqi
# 6 alex
# 7 black_girl
# 8 1
# 9 2
# 10 3
# 11 4
# 12 2
# 13 5
# 14 6
# 15 2


#11.循环names列表，打印每个元素的索引值和元素，当索引值为偶数时，把对应的元素改为-1
print(names)
for index,item in enumerate(names):
    if index%2 ==0:
        names[index] = -1
#0 old_driver
# 2 ['oldboy', 'oldgirl']
# 4 姗姗
# 6 alex
# 8 1
# 10 3
# 12 2
# 14 6
        print(index,item)
print(names) #[-1, 'rain', -1, 'jack', -1, 'peiqi', -1, 'black_girl', -1, 2, -1, 4, -1, 5, -1, 2]


#12.names里有3个2，请返回第二个2的索引值
s = names[names.index(2)+1:].index(2)+names.index(2)+1 #先查找出第一个2，然后从第一个2后面第一位数后开始切片，再查找第二个2，第二个2 的索引值应该大于等于两次查找出来的2和，另外由于切片后都是从0开始计数，故之后还要+1
print(s) #12

#13.现有商品列表如下：
#products={["Iphone8",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",80],["Nike Shoes",799]}

# products=[["Iphone8",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",80],["Nike Shoes",799]]
# print("------商品列表------")
# for x,y in enumerate(products):
#     print(x,y[0],y[1])

#14 写一个循环，不断的问客户想买什么，用户选择一个编号，就把对应的商品添加到购物车，最终用户输入q退出时，打印购物车商品列表
#我的解答：
products=[["Iphone8",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",80],["Nike Shoes",799]]
print("------商品列表------")
for x,y in enumerate(products):
    print(x,y[0],y[1])

shopcarts=[]
exit_flag = False #标志位
while not exit_flag: #表示不退出程序
    consumer_choice=input("请输入您想要购买的商品编号")
    if consumer_choice.isdigit() == True: #判断输入的值是不是数字，==True也可省略
        if int(consumer_choice)>=0 and int(consumer_choice)<=5: #添加条件数值在0-5之间
            shopcarts.append(products[int(consumer_choice)]) #将输入的值，存储到shopcarts列表里
            print("已将商品 %s 加入购物车." %(products[int(consumer_choice)]))
        else:
            print("你好，该商品不存在")
    elif consumer_choice=="q":
        print("----您购买了以下商品")
        for index,item in enumerate(shopcarts):
            print(index,item[0],item[1])
        exit_flag=True
    else: #当输入的为非数字，提示非法
        print("你好,您输入的值非法,请输入数字")

#老师的解答:
products=[["Iphone8",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",80],["Nike Shoes",799]]
shoppin_cart=[]
exit_flag = False #标志位
while not exit_flag:
    print("------商品列表------")
    for index, p in enumerate(products):
        print("%s   %s   %s" %(index,p[0],p[1]))
    chioce = input("请输入想买的商品编号：")
    if choice.isdigit():
        choice = int(choice)
        if choice >= 0 and choice <= len(products):
            shoppin_cart.append(products[choice])
            print("您已将 %s 加入购物车。" %(products[chioce]))
        else:
            print("商品不存在")
    elif choice=="q":
        if len(shoppin_cart)>0: #判断shopping_cart是否有内容，没有就直接退出
            print("-----您已购买以下商品-----")
            for index, p in enumerate(products):
                print("%s %s %s" %(index,p[0],p[1]))
        exit_flag=True





