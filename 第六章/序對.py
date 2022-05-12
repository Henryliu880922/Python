"""
序對是由一連串資料所組成、有順序且不可改變內容的序列。序對的前後以小括號標示，裡面的資料以逗號隔開，資料的型別可以不同
序對和串列相似，差別在於序對不可改變內容，無論是加入、刪除、排序或變更元素等都不被允許，因此序對可以用來存放一些不會變更的資料，而且序對的執行效率比串列好
"""

print((1,"Taipei",2,"Tokyo")) # 包含4個元素的序對
print((2,"Taipei",1,"Tokyo")) # 元素相同但順序不同，表示不同序對

tuple1=tuple()
print(tuple1)
tuple2=tuple((1,2,3))
print(tuple2)
tuple3=tuple("ABCA") # 從字串建立序對
print(tuple3)
tuple4=tuple(range(5)) # 從Range物件建立序對
print(tuple4)
tuple5=(tuple([i * 2 for i in range(5)]))
print(tuple5)

"""
序對支援所有共同的序列運算，前面介紹的len()、max()、min()和sum()等內建函式均適用序對，而random.shuffle()因為涉及變更元素的順序，所以不適用於序對
"""
T=(1,2,3,4,5)
print(len(T))
print(max(T))
print(min(T))
print(sum(T))

print((1,2,3)+("Taipei","Tokyo","Vienna")) # 連結運算子(+)
print(3*(1,2,3)) # 重複運算子(*)
print((1,2,3)*3)
print((1,"小美","大明")==("小美","大明",1)) # 比較運算子
print((1,2,3)!=(1,2,3,4))
print((1,2,3)<(1,2,3,4))
print("Taipei"in(1,"Taipei",2,"Tokyo")) # in 與not in 運算子
print("Taipei"not in(1,"Taipei",2,"Tokyo"))
D=(5,10,15,20,25,30,35,40,45,50)
print(D[0])
print(D[2:5])
print(D[6:-1])

"""
tuple.index 傳回參數所指定的元素第一次出現在序對中的索引
tuple.count 傳回參數所指定的元素出現在序對中的次數
"""
S=(50,20,40,20,30,20,10)
print(S.index(20))
print(S.count(20))

"""
序對和字串、range物件、串列可以一樣做為迭代的物件，將序對做為迭代的物件，然後用For迴圈逐一取出每個元素相加在一起
"""
# 此處的D為上面的變數D
sum=0
for i in D:
    sum=sum+i
print(sum)