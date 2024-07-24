##
# 本程序把一个整数转换为对应的英文名称
#

def main():
    value = int(input("Please enter a positive integer <1000: "))
    print(intName(value))

## 把数值转换为对应的英文名称
# @param number 一个小于1000的正整数
# @return 数值number的名称（例如，"two hundred seventy four")
#
def intName(number)
    part = number # 尚需转换的部分
    name = "" # 数值的名称

    if part >=100:
        name = digitName(part // 100) + "hundred"
        part = part % 100

    if part >=20:
        name = name + " " + tensName(part)
        part = part % 10

    elif part >=10:
        name = name + " " + digitName(part)

    if part >0:
        name = name + " " + digitName(part)

    return name

## 把单个数字转换为对应的英文名称
# @param digit 一个介于1~9的整数
# @return 数字digit的英文名称("one"..."nine")
#
def digitName(digit):
    if digit ==1 : return "one"
    if digit ==2 : return "two"
    if digit ==3 : return "three"
    if digit ==4 : return "four"
    if digit ==5 : return "five"
    if digit ==6 : return "six"
    if digit ==7 : return "seven"
    if digit ==8 : return "eight"
    if digit ==9 : return "nine"
    return ""

## 把介于10~19的整数转换其对应的英文名称
# @param number 一个介于 10~19的整数
# @return 返回给定值number的英文名称("ten"..."nineteen")
#
def teensName(number):
    if number == 10: return "ten"
    if number == 11: return "eleven"
    if number == 12: return "twelve"
    if number == 13: return "thirteen"
    if number == 14: return "fourteen"
    if number == 15: return "fifteen"
    if number == 16: return "sixteen"
    if number == 17: return "seventeen"
    if number == 18: return "eighteen"
    if number == 19: return "nineteen"
    return ""

## 给出介于20~99的数值的十位数英文名称
# @param number 一个介于20~99的整数
# @return 返回给定值number的英文名称（"twenty"..."ninety")
