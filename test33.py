##
#  本程序计算两个立方体的体积
#
def main():
    result1 = cubeVolume(2)
    result2 = cubeVolume(10)
    print("A cube with side length 2 has volume",result1)
    print("A cube with side length 10 has volume",result2)

## 计算一个立方体的体积
# @param sideLength 立方体的边长
# @return 立方体的体积
#
def cubeVolume(sideLength):
    volume = sideLength ** 3
    return volume

# 启动程序
main()