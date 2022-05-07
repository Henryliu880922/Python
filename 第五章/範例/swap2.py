def swap(x):
    temp=x[0]
    x[0]=x[1]
    x[1]=temp

a=[1,2] # 將變數a的值設定為串列[1,2]
print(a) # 印出變數a的元素在交換之前的值
swap(a) # 呼叫swap()函式將參數的元素交換
print(a) # 印出變數a的元素在交換之後的值