## 打印列表
A = ['1','2','3']
B = ['输入1退出','输入10一下的数字不能计算','只能计算10以上的数字']
print(A[0]+'.'+B[0])
print(A[1]+'.'+B[1])
print(A[2]+'.'+B[2])

while True:                                                         ## True 死循环
    Input1 = input("请输入第一次数字：")
    Input1 = int(Input1)
    # 判断 第一次数字大于10 则继续计算
    if Input1 > 10:
        # 声明 Input2为全局变量
        global Input2
        Input2 = int(input("请输入第二次数字:"))
        print(Input1 + Input2)
    # 判断 第一次数字等于1 则退出
    elif Input1 == 1:
        print("退出本次计算")
        break                                                       ## 直接跳出循环
    # 否正重新输入
    else:
        print("输入的数字小于等于10,请重新输入")
        continue                                                    ## 结束当前循环,重新循环