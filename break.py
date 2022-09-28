A = ['(输入 "q" 退出)']

while True:
    Pen = input("请输入文字{}:".format(A[0]))           ## {} .format(A[0])  在"" 里面使用变量
    # Pen = eval(Pen)
    # try:
    #     Pen=eval(Pen)
    # except NameError:
    #     Pen=Pen
    # else:
    #     Pen=eval(Pen)
    if Pen == "q":                                    ## 判断输入的数据是否为 q  q==退出
        break
    elif type(Pen) == int:
        continue                                      ## 结束循环 退出代码
    print(Pen)
