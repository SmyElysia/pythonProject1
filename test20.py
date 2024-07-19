##
# 本程序计算投资收益翻倍所需的时间
#

# 创建常量变量
RATE=5.0
INITIAL_BALANCE=10000.0
TARGET=2 * INITIAL_BALANCE

# 初始化用于循环的变量
balance=INITIAL_BALANCE
year=0

# 计算投资收益翻倍需要的年份
while balance < TARGET:
    year=year+1
    interest= balance * RATE /100
    balance= balance + interest

# 打印结果
print("The investment doubled after",year,"years.")