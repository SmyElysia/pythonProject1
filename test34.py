##
# 本程序定义一个计算金字塔体积的函数
# 并为该函数提供了单元测试
#

def main():
    print("Volume:",pyramidVolume(9,10))
    print("Expected:300")
    print("Volume:",pyramidVolume(0,10))
    print("Expected:0")

## 计算底部为正方形的金字塔的体积
# @param height 表示金字塔高度的浮点数
# @param baseLength
# the pyramid's base
# @return 金字塔的体积，类型为浮点数
#
def pyramidVolume(height,baseLength):
    baseArea = baseLength * baseLength
    return height * baseArea / 3

# 启动程序
main()