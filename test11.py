##
#本程序使用简化的所得税计算表计算所得税
#

#初始化常量，用于税率和税率收入限制
RATE1=0.10
RATE2=0.25
RATE1_SINGLE_LIMIT=32000.0
RATE1_MARRIED_LIMIT=64000.0

#读取收入和婚姻状况
income=float(input("请输入你的收入： "))
maritalStatus=input("请输入s代表单身，m代表已婚：")

#计算所得税
tax1=0.0
tax2=0.0

if maritalStatus == "s":
    if income<=RATE1_SINGLE_LIMIT:
        tax1=RATE1*income
    else:
        tax1=RATE1*RATE1_SINGLE_LIMIT
        tax2=RATE2*(income-RATE1_SINGLE_LIMIT)
else:
    if income<=RATE1_MARRIED_LIMIT:
        tax1=RATE1*income
    else:
        tax1=RATE1*RATE1_MARRIED_LIMIT
        tax2=RATE2*(income-RATE1_MARRIED_LIMIT)
totalTax=tax1+tax2
#打印结果
print("税费是%.2f"%totalTax)