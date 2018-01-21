#作业一：
# 基础需求：
# 让用户输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后退出程序
user_name ="Junee"
user_passwd="123123"
count=1
input_name=input("请输入你的用户名：")
if input_name==user_name:
    while count <= 3:
        input_passwd=input("您好，请输入您的密码：")
        if input_passwd==user_passwd:
            print("您好！欢迎您的登录！")
            break
        else:
            print("您好，您输入的密码不正确，还可以输入 %d 次：" %(3-count))
        count+=1

else:
    print("您好，不存在您所输入的用户！")

# 升级需求：
# 可以支持多个用户登录 (提示，通过列表存多个账户信息)
# 用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）

user_name =["Junee","Wynnie","Alex","GYC"]
user_passwd=["123123","234234","345345","456456"]
count=1
input_name=input("请输入你的用户名：")
with open("blacklist.txt", "r") as f:
    block_user = f.readlines()
    f.close()
    if input_name in block_user:
        print("对不起，您所输入的用户已经加入黑名单")
        exit_flag = True
    else:
        f.close
        if input_name in user_name:
            while count <= 3:
                input_passwd=input("您好，请输入您的密码：")
                if input_passwd == user_passwd[user_name.index(input_name)]:
                    print("您好！欢迎您的登录！")
                    break
                else:
                    print("您好，您输入的密码不正确，还可以输入 %d 次：" %(3-count))
                count += 1
            if count==4:
                with open("blacklist.txt", 'w') as f:
                    f.write("%s" %input_name)
                    print("该用户已被加入黑名单")
                    f.close()
                    exit_flag=True

        else:
            print("您好，不存在您所输入的用户！")