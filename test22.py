##
# 本程序用于处理用户输入的一系列成绩
# 计算成绩合格的人数和成绩不合格的人数
# 计算平均成绩，查找最高成绩和最低成绩
#

# 初始化计数器变量
numPassing= 0
numFailing= 0

# 初始化用于计算平均成绩的变量
total= 0
count= 0

# 初始化最高成绩和最低成绩变量
minGrade = 100.0  # 假设最高分为100
maxGrade = 0.0

# 使用while循环读取成绩
grade = float(input("Enter your grade or -1 to finish: "))
while grade >= 60.0 :
    # 递增成绩合格人数的计数器和成绩不合格人数的计数器
    if grade >= 60.0 :
        numPassing = numPassing + 1
    else:
        numFailing = numFailing + 1
    # 判断成绩是否为最低成绩或者最高成绩
    if grade < minGrade:
        minGrade =grade
    if grade > maxGrade:
        maxGrade = grade
    # 把成绩累加到累计汇总变量total中
    total =total + grade
    count = count + 1

    # 读取下一个成绩
    grade = float(input("Enter your grade or -1 to finish: "))

# 打印结果
if count > 0:
    average=total/count
    print("The average grade is %.2f" % average)
    print("Number of passing grades is",numPassing)
    print("Number of failing grades is",numFailing)
    print("The maximum grade is %.2f"% maxGrade)
    print("The minimum grade is %.2f"% minGrade)