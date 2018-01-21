

# 作业题目（二）：购物车程序
# 作业需求：
# 数据结构：
goods =[
    {"name":
         "电脑", "price": 1999},
    {"name":
         "鼠标", "price": 10},
    {"name":
         "游艇", "price": 20},
    {"name":
         "美女", "price": 998}
]
# 功能要求：
# 基础要求：
#
# 1、启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
# 2、允许用户根据商品编号购买商品
# 3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
# 4、可随时退出，退出时，打印已购买商品和余额
# 5、在用户使用过程中，
# 关键输出，如余额，商品已加入购物车等消息，需高亮显示
# 扩展需求：
# 1、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
# 2、允许查询之前的消费记录

import os
user_info={"Alex":"123123","egon":"345345","jay":"678678"}
name=input("login：")
pwd=input("password：")
shopping_list=[]
wage=0
has_file = False#判断用户购物历史文件是否存在
if name in user_info.keys(): #判断用户登录的名字是否在字典中
    if pwd == user_info.get(name): #判断用户登录密码是否和用户登录名匹配
        if os.path.exists("购物车_"+name+".txt"): #判断文件是否存在
            has_file = True #标志位
            file = open("购物车_"+name+".txt", "r",encoding='utf8') #文件以utf-8的编码打开
            file.readline()
            balanceInfo = file.readline()
            shoppingHistory = file.readline()
            wage=balanceInfo.split("::")[1]
            wage= int(wage)
            shopping_list =eval(shoppingHistory.split("::")[1])
            print("当前余额:", int(wage))
            print("----购物历史-----:")
            for index,items in enumerate(shopping_list) :
                print("%s"  " %s"  "%s" %(index,items["name"],items["price"]))
            file.close()
        print("欢迎登录！")
    else:
        print("您好，密码不正确。")
else:
    print("对不起，不存在该用户。")
    exit_flag=True
if  has_file == False:
    wage=input("Your Wage：")
    wage = int(wage)

while True:
        print("----商品列表----")
        for index,commodity in enumerate(goods):
            print(index,commodity["name"],commodity["price"])
        commodity_num=input("请输入您想购买的商品编号：")
        if commodity_num.isdigit():
            commodity_num=int(commodity_num)
            if commodity_num in range(0,len(goods)):
                if int(goods[commodity_num]["price"])<= wage:
                    shopping_list.append(goods[commodity_num])
                    wage=int(wage)-int(goods[commodity_num]["price"])
                    print(" \033[1;32;43m 商品 %s 已加入购物车 \033[0m!,还剩余\033[1;33;44m %d \033[0m 元" %(goods[commodity_num]["name"],wage))
                else:
                    print("您的余额不足，无法购买")
            else:
                print("您好，不存在您所输入的商品。")
        else:
            print("请输入数字")

        select_choice=input("是否“退出”？ Y or anykey continue ？")
        if select_choice=="Y":
            if len(shopping_list)>0:
                print("当前用户： %s" %name)
                print("----您已购买以下商品----")
                for index,items in enumerate(shopping_list):
                    print(index+1,items["name"],items["price"])
                print("--本次余额 %d 元--" %wage)
                file = open("购物车_"+name+".txt", "w",encoding="utf-8")
                file.write("username::%s\nrest_wage::%d\nshoppint_history::%s" %(name,wage,shopping_list))
                file.close()
                break
            else:
                print("您还未购买任何商品。")
                break



