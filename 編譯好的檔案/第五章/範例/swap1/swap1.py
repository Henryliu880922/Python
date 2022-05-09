def swap(x,y):
    temp=x
    x=y
    y=temp

a,b=1,2 # 將變數a,b的值設定為數值1,2
print(a,b) # 印出a,b在交換之前的值
swap(a,b) # 呼叫swap()函式將兩個參數的值交換
print(a,b) # 印出a,b在交換之後的值 