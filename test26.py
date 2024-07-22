##
# 本程序通过用户读取考试成绩
# 绘制一个成绩分布直方图
#

from matplotlib import pyplot as plt
# 初始化用于保存成绩等级计数的变量
numAs=0
numBs=0
numCs=0
numDs=0
numFs=0

# 使用带预读取的while循环读取考试成绩
grade = int(input("Enter exam grade or -1 to finish:"))
while grade>=0:
    if grade>=90.0:
        numAs=numAs+1
    elif grade>=80.0:
        numBs=numBs+1
    elif grade>=70.0:
        numCs=numCs+1
    elif grade>=60.0:
        numDs=numDs+1
    else:
        numFs=numFs+1
    grade=int(input("Enter exam grade or -1 to finish:"))

    # 绘制成绩直方图
    plt.bar(1,numAs)
    plt.bar(2,numBs)
    plt.bar(3,numCs)
    plt.bar(4,numDs)
    plt.bar(5,numFs)

    # 添加坐标轴标签
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")

    # 添加表示学生人数的标题
    numStudents = numAs+numBs+numCs+numDs+numFs
    plt.title("%d students\nGrade Distribution"% numStudents)

    # 在条形图下面添加字母，作为坐标轴刻度标签
    plt.xticks([1.4,2.4,3.4,4.4,5.4],["A","B","C","D","F"])

    # 显示图表
    plt.show()