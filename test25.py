##
# 本程序计算若干名学生的平均考试成绩
#

# 读取每名学生的考试成绩
numExams=int(input("How many exam grades does each student have?"))

# 初始化moreGrades为一个非哨兵值
moreGrades="Y"

# 循环计算平均考试成绩，直到用户做出选择终止为止
while moreGrades=="Y":

    # 为一名学生计算平均成绩
    print("Enter the exam grades.")
    total=0
    for i in range(1,numExams+1):
        score=int(input("Exam %d:" %i)) # 提示输入每次考试的成绩
        total=total+score

    average=total/numExams
    print("The average grade is %.2f" % average)
    moreGrades=input("Enter exam grades for another student(Y/N)?")
    moreGrades=moreGrades.upper()