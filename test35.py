from random import randint
## 生成一个随机密码
# @param length  表示密码长度的一个整数
# @return  给定长度的密码字符串
# 至少包含一位数字和一个特殊字符
#

# 返回从给定的字符串中随机选取的一个字符
# @param characters 用于随机选择字符的字符串
def randomCharacter(characters):
    # 把一个字符串插入到另一个字符串的随机位置
    # @param string 应该插入到另一个字符串中的字符串
    # @param toInsert 要插入的字符串
    # @return 插入toInsert到string后的结果字符串
    #
    n = len(characters)
    r = randint(0,n,-1)
    return characters[r]
def insertAtRandom(string,toInsert):
    n = len(string)
    r = randint(0,n)
    result = ""
    for i in range(r):
        result += string[i]
    result = result + toInsert
    for i in range(r,n):
        result = result + string[i]
    return result
def makePassword(length):
    password = ""
    for i in range(length - 2):
        password = password + randomCharacter("abcdefghijklmnopqrstuvwxyz")
    randomDigit = randomCharacter("0123456789")
    randomSymbol = randomCharacter("+-*/?!@#$%&")
    password = insertAtRandom(password,randomSymbol)
    return password


# 测试函数1
def main():
    for i in range(10):
        print(randomCharacter("abcdef"),end="")
    print()

def randomCharacter(characters):
    n = len(characters)
    r = randint(0, n-1)
    return characters[r]

main()

# 测试函数2
def main():
    for i in range(10):
        print(insertAtRandom("arxcsw","8"))

def insertAtRandom(string,toInsert):
    n = len(string)
    r = randint(0,n)
    result=""

    for i in range(r):
        result += string[i]
    result = result + toInsert
    for i in range(r,n):
        result = result + string[i]

    return result

main()