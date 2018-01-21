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

while True:
    for k in menu:
        print(k)
    choice=input(">：").strip()
    if not choice: continue

    if choice in menu:
        for k in menu[choice]:
            while True:#进入第2层
                print (k)
            choice2 = input(">>：").strip()
            if not choice2: continue
            if choice2 in menu[choice]:
                print("GO TO:",menu[choice][choice2])
                while True:#进入第3层
                    for k in menu[choice][choice2]:
                        print(k)
                    choice3 = input(">>>:").strip()
                    if not choice3: continue
                    if choice3 in menu[choice][choice2]:
                        print("GO TO:", menu[choice][choice2][choice3])
                    elif choice3=="b":
                        break
                    elif choice3 == "q":
                        exit("Bye.")
                    else:
                        print("节点不存在")
            elif choice2 =="b":
                break
            elif choice2 == "q":
                exit("Bye.")
            else:
                print("节点不存在")




