##
# 本程序模拟投掷两个骰子
#

from random import randint

for i in range(10):
    # 生成两个位于1（包含）~6（包含）的整数
    d1=randint(1,6)
    d2=randint(1,6)

    # 打印两个值
    print(d1,d2)