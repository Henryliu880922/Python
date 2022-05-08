grade=[[95,100,100],[86,90,75],[98,98,96],[78,90,80],[70,68,72]]
for i in range(5):
    subtotal=0 # 將用來暫存總分數的變數subtotal歸零
    for j in range(3): # 將分數累加的總分暫存在變數subtotal
        subtotal+=grade[i][j]
    grade[i].append(subtotal) # 將總分加入二維串列
for i in range(5):
    print("學生",i+1,"的總分為",grade[i][3])