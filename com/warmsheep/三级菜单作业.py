# 作业题目（一）：三级菜单
# 作业需求：
# 数据结构：
#
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
#
# 需求：
# 1.可依次选择进入各子菜单
# 2.可从任意一层往回退到上一层
# 3.可从任意一层退出程序
# 4.所需新知识点：列表、字典
#方法二：

count=1
while count<=5:
    if count == 1:
        city=input("进入第 %d 级菜单，请输入 %s ：" %(count,menu.keys()))
        if city in menu.keys():
            print("%s 下面有这些 %s 区："%(city,menu.get(city).keys()))
        else:
            count -= 1
            print("不存在您所输入的城市")
    elif count == 2:
        area=input("进入第 %d 级菜单,请输入 %s ：" %(count,menu.get(city).keys()))
        if area in  menu.get(city).keys():
            print("%s 下面有这些 %s 街道" %(area,menu.get(city).get(area).keys()))
        else:
            count -= 1
            print("不存在您所输入的区域")
    elif count == 3:
        street=input("进入第 %d 级菜单,请输入 %s ：" %(count,menu.get(city).get(area).keys()))
        if street in menu.get(city).get(area).keys():
            print("%s 下面有这些 %s 公司" %(street,menu.get(city).get(area).get(street).keys()))
        else:
            count -= 1
            print("不存在您所输入的街道")
    elif count==4:
        company=input("进入第 %d 级菜单,请输入 %s ：" %(count,menu.get(city).get(area).get(street).keys()))
        if company in menu.get(city).get(area).get(street).keys():
            print("%s 下面有这些 %s 内容" %(company,menu.get(city).get(area).get(street).get(company)))
        else:
            count -= 1
            print("不存在您所输入的公司")

    select_choice=input("下一步操作: [继续/退回/退出]: ")
    if select_choice=="退出":
        break
    elif select_choice=="退回":
        count-=1
        if count<1:
            count=1
    elif select_choice=="继续":
        count += 1
        if count>4:
            count=4
    else:
        print("选项不存在！默认继续")
        if  count < 5:
            count+= 1
count+=1






# #方法一
# current_level = 1
# temp_keys = list(menu.keys())
# level_one_condition = ""
# level_two_condition = ""
# level_three_condition = ""
# level_four_codition = ""
# while True :
#     has_error = False
#     if current_level == 5:
#         print("没有下一级菜单")
#     elif current_level == 0:
#         current_level = 1
#
#     if(current_level == 1):
#         input_condition = input("请输入您想查询的省或者自治区: %s:  " % temp_keys)
#         level_one_condition = input_condition
#     elif(current_level == 2):
#         input_condition = input("请输入您想查询的区: %s:  " % temp_keys)
#         level_two_condition = input_condition
#     elif(current_level == 3):
#         input_condition = input("请输入您想查询的街道: %s: " % temp_keys)
#         level_three_condition = input_condition
#     elif(current_level == 4):
#         input_condition = input("请输入您想查询的公司: %s: " % temp_keys)
#         level_four_codition = input_condition
#
#     if (current_level == 1):
#         if level_one_condition in list(menu.keys()):
#             print("输入正确！")
#         else:
#             print("您好，不存在您所输入的省或自治区！")
#             has_error = True
#     elif (current_level == 2):
#         if level_two_condition in list(menu.get(level_one_condition).keys()):
#             print("输入正确！")
#         else:
#             print("您好，不存在您所输入的区或县！")
#             has_error = True
#     elif (current_level == 3):
#         if level_three_condition in list(menu.get(level_one_condition).get(level_two_condition).keys()):
#             print("输入正确！")
#         else:
#             print("您好，不存在您所输入的街道！")
#             has_error = True
#     elif (current_level == 4):
#         if level_four_codition in list(menu.get(level_one_condition).get(level_two_condition).get(level_three_condition).keys()):
#             print("输入正确！")
#         else:
#             print("您好，不存在您所输入的公司！")
#             has_error = True
#     select_condition = input("下一步操作: [继续/退回/退出]: ")
#     if (select_condition == "退出"):
#         break
#     elif (select_condition == "退回"):
#         current_level = current_level - 1
#         if (current_level < 1):
#             current_level = 1
#         if(current_level > 5):
#             current_level = 5
#     elif (select_condition == "继续"):
#         if has_error == False and current_level < 5:
#             current_level = current_level + 1
#         if(current_level < 1):
#             current_level = 1
#         if (current_level > 5):
#             current_level = 5
#     else:
#         print("选项不存在！默认继续")
#         if has_error == False and current_level < 5:
#             current_level = current_level + 1
#
#     if(current_level == 1):
#         temp_keys = list(menu.keys())
#     if (current_level == 2):
#         temp_keys = list(menu.get(level_one_condition))
#     elif (current_level == 3):
#         temp_keys = list(menu.get(level_one_condition).get(level_two_condition))
#     elif (current_level == 4):
#         temp_keys = list(menu.get(level_one_condition).get(level_two_condition).get(level_three_condition))
#     elif (current_level == 5):
#         temp_keys = list(menu.get(level_one_condition).get(level_two_condition).get(level_three_condition).get(level_four_codition))



