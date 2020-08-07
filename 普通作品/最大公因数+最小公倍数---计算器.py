import time
import os
for i in range(10):
    question1 = int (input("第一个数:"))
    a = question1
    question2 = int (input("第二个数:"))
    b = question2
    answer = question1 % question2
    while (answer != 0):
        question1 = question2
        question2 = answer
        answer = question1 % question2
    print("最大公因数：",question2)
    #---------------分割线---------------#
    c = a / question2
    d = b / question2
    e = c * d * question2
    int(e)
    print("最小公倍数:",e)

    time.sleep(5)
