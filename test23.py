##
# 本程序打印一张表格，显示投资收益增长
#

# 定义常量
RATE =5.0
INITIAL_BALANCE=10000.0

# 读取用于计算的年份
numYears = int(input("Enter the number of years: "))

# 打印一张表格，显示各年份的账户余额
balance = INITIAL_BALANCE
for year in range(1,numYears+1):
    interest = balance * RATE / 100
    balance = balance + interest
    print("%4d %10.2f" % (year, balance))

