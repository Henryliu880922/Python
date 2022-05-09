num=eval(input("請輸入1~100的整數："))
result=1 # 將變數result的初始值設定為1，用來存放階層值
i=1 # 將變數i的初始值設定為1，用來做為計數器

while i<= num: # 當i小於等於num時，就將i累乘到result，再將i遞增1
    result=result*i
    i=i+1
print(num,"階乘的值為",result)