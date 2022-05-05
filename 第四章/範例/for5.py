import re


num=eval(input("請輸入1~100的正整數："))
result=1
for i in range(1,num+1):
    result=result*i
print(num,"階乘的值為",result)