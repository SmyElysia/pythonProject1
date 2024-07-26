##
# 本程序演示如何使用递归函数打印三角形
#

def main():
    printTriangle(4)

## 打印一个给定边长的三角形
# @param sideLength 一个表最下面一行长度的整数
#
def printTriangle(sideLength):
    if sideLength <1 : return
    printTriangle(sideLength-1)

    # 在最下面打印一行
    print("[]"*sideLength)

# 启动程序
main()
