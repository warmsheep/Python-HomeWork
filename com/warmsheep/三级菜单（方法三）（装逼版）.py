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

current_layer=menu
layers=[]#记录每次的选择操作
while True:
    for k in current_layer:
        print(k)
    choice=input(">:").strip()
    if not choice:continue
    if choice in current_layer:
        layers.append(current_layer)
        current_layer=current_layer[choice]
    elif choice=="b":
        if len(layers)>0:
            current_layer=layers.pop()
        else:
            print("已是顶层！")
    elif choice == "q":
        break

