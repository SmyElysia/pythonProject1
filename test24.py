##
# 本程序打印一个表格，显示x的幂次
#

# 初始化表示访范围最大值的常量
NMAX =4
XMAX=10

# 打印表格标题
for n in range(1,NMAX+1):
    print("10%d"%n,end="")

print()
for n in range(1,NMAX+1):
    print("%10s"%"x",end="")
print("\n","    ","-"*35)\

# 打印表格内容
for x in range(1,XMAX+1):
    # 打印表格中x行的内容
    for n in range(1,NMAX+1):
        print("%10.0f"% x **n,end="")
    print()