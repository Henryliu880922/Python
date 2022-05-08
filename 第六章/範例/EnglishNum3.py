EnglishNum=["One","Two","Three","Four","Five"] # 串列變數EnglishNum用來存放1~5的英文
num=eval(input("請輸入1~5的整數："))

if num in range(1,6): # 若輸入的整數介於1~5，就印出對應的英文，否則印出超出範圍
    print(EnglishNum[num-1])
else:
    print("您輸入的資料超過範圍！")