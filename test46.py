##
# 本程序读取一系列数值，缩放后按相反顺序打印输出
#

def main():
    numbers = readFloats(5)
    multiply(numbers,10)
    printReversed(numbers)

## 读取一系列浮点数
# @param numberOfInputs 要读取的输入值个数
# @return 一个包含输入值的列表
#
def readFloats(numberOfInputs):
    print("Enter",numberOfInputs,"numbers:")
    inputs = []
    for i in range(numberOfInputs):
        value = float(input(""))
        inputs.append(value)

    return inputs

## 把列表的所有元素乘以一个因子
# @param values 一个值的列表
# @param factor 用于相乘的因子值
#
def multiply(values,factor):
    for i in range(len(values)):
        values[i] = values[i] * factor

## 按相反的顺序打印列表的元素
# @param values 一个值的列表
#
def printReversed(values):
    # 以相反的顺序遍历列表，从最后一个元素开始
    i = len(values) - 1
    while i >= 0:
        print(values[i],end=' ')
        i=i-1
    print()
# 启动程序
main()
