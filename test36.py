##
# 本程序演示可复用函数的用法
#

def main():
    print("Please enter a time: hours, then minutes.")
    hours = readIntBetween(0, 23)
    minutes = readIntBetween(0, 59)
    print("You entered %d hours and %d minutes." % (hours, minutes))

## 重复提示用户输入一个值
# 直到用户输入一个有效值（位于给定区间）
# @param low 表示允许输入的最小整数值
# @param high 表示允许输入的最大整数值
# @return 用户输入的整数值，范围为 low(包含）~ high（包含）
#
def readIntBetween(low, high):
    value = int(input("Enter a value between " + str(low) + " and " +
                     str(high) + ": "))
    while value < low or value > high:
        print("Error: value out of range.")
        value = int(input("Enter a value between " + str(low) + " and " +
                          str(high) + ": "))
    return value

if __name__ == "__main__":
    main()
