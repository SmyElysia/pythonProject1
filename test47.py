##
# 本程序基于一系列测验分数计算最终成绩
# 舍弃两个最低分数，计算剩余分数的累加和。程序使用了一个列表
#

def main():
    scores = readFloats()
    if len(scores) >1:
        removeMinimum(scores)
        removeMinimum(scores)
        total = sum(scores)
        print("Final score:",total)
    else:
        print("At least two scores are required.")

## 读取一系列浮点数
# @return 一个包含数值的列表
#
def readFloats():
    # 创建一个空列表
    values = []

    # 读取输入到列表values中
    print("Please enter values,Q to quit:")
    userInput = input("")
    while userInput.upper()!= "Q":
        values.append(float(userInput))
        userInput = input("")

    return values

## 从列表中删除最小值
# @param values  一个大小>=1的列表
#
def removeMinimum(values):
    smallestPosition = 0
    for i in range(len(values)):
        if values[i]< values[smallestPosition]:
            smallestPosition = i

    values.pop(smallestPosition)

# 启动程序
main()
