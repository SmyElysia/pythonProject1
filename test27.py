##
# 本程序为多项选择题考试测试评分
# 每道题有4个可能的选择：a、b、c或者d
#

# 定义包含正确答案的字符串
CORRECT_ANSWERS = "adbdcacbdac"

# 读取用户的答案，确保提供了足够数量的答案
done=False
while not done:
    userAnswers=input("Enter your exam answers:")
    if len(userAnswers)==len(CORRECT_ANSWERS):
        done=True
    else:
        print("Error: an incorrect number of answers given.")

# 批改考试结果
numQuestions=len(CORRECT_ANSWERS)
numCorrect=0
results=""

for i in range(numQuestions):
    if userAnswers[i]==CORRECT_ANSWERS[i]:
        numCorrect+=1
        results+=userAnswers[i]
    else:
        results+="X"

# 给出考试成绩
score=round(numCorrect/numQuestions*100)

if score==100:
    print("Very good!")
else:
    print("You missed %d questions:%s"%(numQuestions-numCorrect,results))
print("Your score is %d percent"%score)