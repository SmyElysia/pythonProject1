# 求素数

def main():
    n = int(input("Please enter the upper limit:"))
    if n >=2 :
        print(2)
    i=3
    while i <= n:
        if isprime(i):
            print(i)
        i = i + 2

# 测试一个整数是否为素数
# @param n为任意正整数
# @return 如果n为素数，返回True；否则返回False
def isprime(n):

    if n ==1:
        return False

    if n ==2 :
        # 2是素数
       return True

    if n % 2 == 0 :
        # 2以外的偶数都不是素数
       return False

    # 尝试查找可以整除n的数

    k=3 # n是奇数，故不能被2整除
    # 仅需要尝试直到sqrt(n)的除数
    while k * k <= n:
        if n % k == 0 :
            # n不是素数，因为可以被k整除
            return False
        # 尝试下一个奇数
        k = k + 2

    # 没有发现可整除的除数，因此n是素数
    return True

# 启动程序
main()