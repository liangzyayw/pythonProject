# 设置变量
Input1 = int(input("请输入第一次数字:"))

# 简单计算器
# 判断 第一次数字小于10 不可计算
if Input1 < 10:
    print("计算不了,请重新输入")
# 判断 第一次数字大于10 则继续计算
elif Input1 > 10:
    # 声明 Input2为全局变量
    global Input2
    Input2 = int(input("请输入第二次数字:"))
    print(Input1 + Input2)
