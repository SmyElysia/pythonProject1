##
# 本程序演示了递归函数digitSum
#

def main():
    print("Digit sum:",digitSum(1729))
    print("Expected:19")
    print("Disit sum:",digitSum(1000))
    print("Expected:1")
    print("Digit sum:",digitSum(9))
    print("Expected:9")
    print("Digit sum:",digitSum(0))
    print("Expected:0")

## 计算一个整数中各位数字的累加和
# @param n 一个大于或者等于0的数
# @return 整数n中各位数字的累加和
#
def digitSum(n):
    if n==0 : return 0 # 终止递归的特殊情况
    return digitSum(n//10)+n % 10 # 一般情况

# 启动程序
main()