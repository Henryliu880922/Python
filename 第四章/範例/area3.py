PI=3.1459
radius=eval(input("請輸入圓半徑："))

if radius<0:
    print("圓半徑不得為負數")
else:
    print("半徑為",radius,"的圓面積為",PI*radius*radius)