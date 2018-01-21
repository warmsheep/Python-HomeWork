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
#方法一：
# curren_layer=menu
# layers=[]
# while True:
#     for k in curren_layer:
#         print(k)
#     choice=input(">:")
#     if choice in curren_layer:
#         layers.append(curren_layer)
#         curren_layer=curren_layer[choice]
#     elif choice=="b":
#         if len(layers)>0:
#             curren_layer=layers.pop()
#         else:
#             print("已经是顶层！")
#     elif choice=="q":
#         break
while True:
    for k in menu:
        print(k)
    choice=input(">:").strip()
    if not choice: continue
    elif choice == "b":
        print("已经是顶层。")
    while True:
        if choice in menu:
            for k in menu[choice]:
                print(k)
            choice1=input(">>:").strip()
        if not choice1: continue
        elif choice1 == "b":
            break
        while True:
            if choice1 in menu[choice]:
                for k in menu[choice][choice1]:
                    print(k)
            choice2=input(">>>:").strip()
            if not choice2:continue
            elif choice2 == "b":
                break
            while True:
                if choice2 in menu[choice][choice1]:
                    for k in menu[choice][choice1][choice2]:
                        print(k)
                choice3=input(">>>>:").strip()
                if not choice3:continue
                elif choice3 == "b":
                    break
                while True:
                    if choice3 in  menu[choice][choice1][choice2]:
                        for k in menu[choice][choice1][choice2][choice3]:
                            print(k)
                        choice4=input(">>>>>:").strip()
                        if not choice4:continue
                        elif choice4=="b":
                            break





