##
#本程序模拟邮票自动售货机
#接收美元钞票，吐出一等邮票和一美分邮票
#

#以美分为单位 定义一张一等邮票的单价
FIRST_CLASS_STAMP_PRICE=49

#获取美元钞票数量
dollarStr =input("Enter number of dollars:")
dollars=int(dollarStr)

#计算并打印吐出的邮票数量
firstClassStamps=100*dollars//FIRST_CLASS_STAMP_PRICE
change=100*dollars-firstClassStamps*FIRST_CLASS_STAMP_PRICE
print("First class stamps: %6d"%firstClassStamps)
print("Penny stamps:    %6d"%change)