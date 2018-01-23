# 题目：输出9*9口诀。
#方法一：最丑输出，长方形输出
for x in range(1,10):
    for y in range(1,10):
        print("%d * %d = %2d" %(x,y,x*y),end=" ")
    print("") #print("")表示换行，不输出这句的话输出的乘法表格式错乱
# # 方法二：正三角输出
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print("")

# # 方法二：倒三角输出
for i in range(1,10):
    for k in range(1, i):
        print(end="       ")#由于每个算式所占的位置为7个字节，所以多余前面空出的地方输出相应的空格数，在Python中不能直接写print("      ")语句表示输出空格，必须添加end关键字，表示结尾以等号右边的内容输出，与后面的右上和左上的差别相似。
    for j in range(i,10):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")#乘法算式按行输出，与完整格式相比，内层循环范围为i~9，当外层循环的i逐渐递增时，每行输出的算式个数会越来越少，
    print("")