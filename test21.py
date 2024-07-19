##
# 本程序打印以哨兵值作为结束的一系列值的平均值
#
#

# 初始化变量，保存累加和和计数
total=0.0
count=0

# 初始化salary为任意非哨兵值
salary=0.0

# 处理数据，直到输入了一个哨兵值
while salary>=0.0:
    salary=float(input("Enter a salary or -1 to finish:"))
    if salary>=0.0:
        total=total+salary
        count=count+1
# 计算工资的平均值，并打印结果
if count>0:
    average=total/count
    print("Average salary is",average)
else:
    print("No data was entered.")