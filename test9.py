##
# 本程序演示数值和字符串的比较
#

from math import sqrt

#比较整数
m=2
n=4

if m*m==n:
    print("2 times 2 is four")

#比较浮点数
x=sqrt(2)
y=2.0
if x*x==y:
    print("sqrt(2) times sqrt(2) is 2")
else:
    print("sqrt(2) times sqrt(2) is not two but %.18f" %(x*x))

EPSILON=1E-14
if abs(x*x-y)<EPSILON:
    print("sqrt(2) times sqrt(2) is approximately 2")

#比较字符串
s="120"
t="20"

if s==t:
    comparsion="is the same as"
else:
    comparsion="is not the same as"
print("The string '%s' %s the string '%s'."%(s,comparsion,t))

u="1"+t
if s!=u:
    comparsion="not"
else:
    comparsion=""
print("The string '%s' and '%s' are %sidentical."%(s,u,comparsion))