"""
集合型別用來表示集合，包含沒有順序、沒有重複且可改變內容的多個資料。集合的前後以大括號表示，裡面的資料以逗號隔開，資料的型別可以不同
"""
print({1,"Taipei",2,"Tokyo"})
print({2,"Taipei",1,"Tokyo"})

# 建立集合

set1=set() # 建立空集合
print(set1)
set2=set({1,2,3}) # 建立包含1,2,3的集合
print(set2)
set3={"台北","紐約"} # 建立包含"台北","紐約"的集合
print(set3)

"""
建立空集合不能寫成set1={}，這會建立空字典
我們可以從字串、range物件、串列或序對建立集合
"""
set4=set("ABCA") # 從字串建立集合，'A'不會重複出現
print(set4)
set5=set(range(5)) # 從range物件建立集合
print(set5)
set6=set([i*2 for i in range(5)]) # 從串列解析得到的串列建立集合
print(set6)
S={1,2,3,4,5} # 定義名稱為S、包含5個元素的集合
print(len(S)) # 傳回集合參數S的長度為5
print(max(S)) # 傳回集合參數S中最大的元素為5
print(min(S)) # 傳回集合參數S中最小的元素為1
print(sum(S)) # 傳回集合參數S中元素的總和為15

# 運算子
"""
因為集合中的元素沒有順序之分，因此，集合不支援連結運算子、重複運算子、索引運算子、片段運算子或其他順序相關的運算
集合支援in與not in運算子，用來檢查指定的元素是否存在於集合
"""
S1={"小丸子","小玉","花輪"}
S2={"丸尾","小丸子","小玉","花輪"}
S3={"花輪","小丸子","小玉"}
print(S1==S3)
print(S1!=S2)
print(S1<=S2)
print(S1<S2)
print(S1>=S2)
print(S1>S2)
print(S2>S3)
print(S2>=S3)

"""
可以用for迴圈走訪集合中的元素，使用for迴圈逐一取出每個元素相加在一起
"""
F={5,10,15,20,25,30,35,40,45,50}
sum=0
for i in S:
    sum=sum+i
print(sum)

"""
集合處理方法

集合隸屬於set類別的物件，set類別內建許多集合處理方法
set.add 將參數所指定的元素加入集合
set.remove 從集合中刪除參數所指定的元素，若該元素不存在，將會發生KeyError錯誤
set.pop 從集合中刪除一個元素並傳回該元素
set.copy 傳回集合的複本，這和原來的集合是不同的物件
set.clear 從集合中刪除所有元素
"""
D1={10,20,30,40,50} # 定義名稱為D1、包含5個元素的集合
D1.add(60) # 將元素60加入D1
print(D1)
D1.remove(30) # 從D1中刪除元素30
print(D1)
D1.pop() # 從D1中刪除一個元素並傳回
print(D1)
D2=D1.copy() # 傳回D1的複本並指派給D2
print(D2)
D1.clear() # 從D1中刪除所有元素，D1會變成空集合
print(D1)

"""
子集合/超集合
"""
A1={"小丸子","小玉","花輪"}
A2={"丸尾","小丸子","小玉","花輪"}
print(A1.issubset(A2)) # A1是A2的子集合嗎？傳回True，表示是
print(A1.issuperset(A2)) # A1是A2的超集合嗎？傳回False，表示否
print(A2.issubset(A1)) # A2是A1的子集合嗎？傳回False，表示否

"""
集合運算
set.isdisjoint 若集合和參數S所指定的集合沒有相同的元素，就傳回True，否則就傳回False
set.union 將集合和參數所指定的集合進行聯集，然後傳回新的集合，亦可使用|運算子進行聯集(聯集指的是存在於兩變數的元素)
set.update 將集合和參數所指定的集合進行聯集，然後將結果更新到集合
set.intersection 將集合和參數所指定的集合進行交集，然後回傳新的集合，亦可使用&運算子進行交集(交集指的是存在於兩變數的元素)
set.intersection_update 將集合和參數所指定的集合進行交集，然後將結果更新到集合
set.difference 將集合和參數所指定的集合進行差集，然後回傳新的集合，亦可使用-運算子進行差集(差集指的是存在於兩變數的元素)
set.difference_update 將集合和參數所指定的集合進行差集，然後將結果更新到集合
set.symmetric_difference 將集合和參數所指定的集合進行對稱差集(互斥)，然後回傳新的集合，亦可使用^運算子進行對稱差集(對稱差集指的是存在於一變數但不存在於另一變數)
set.symmetric_difference_update 將集合和參數所指定的集合進行對稱差集(互斥)，然後將結果更新到集合
"""
B1={1,3,5}
B2={3,5,7,9}
print(B1.isdisjoint(B2)) # B1和B2沒有相同的元素嗎？傳回False，表示否
B3=B1.union(B2) # 亦可寫成 B3=B1|B2，表示B3是B1和B2的聯集
print(B1) # B1的內容沒有改變
print(B3) # B3的內容是聯集的結果
B1.update(B2) # B1的內容更新成聯集的結果

B4=B1.intersection(B2) # 亦可寫成B4=B1&B2，表示B4是B1和B2的交集
print(B1) # B1的內容沒有改變
print(B4) # B4的內容是交集的結果
B1.intersection_update(B2) # 將B1和B2進行交集的結果更新到B1
print(B1) # B1的內容更新成交集的結果

B3=B1.difference(B2) #亦可寫成B3=B1-B2
print(B1) # B1的內容沒有改變
print(B3) # B3的內容是差集的結果
B1.difference_update(B2) # 將B1和B2進行差集的結果更新到B1
print(B1) # B1的內容更新成差集的結果

B3=B1.symmetric_difference(B2) #亦可寫成B3=B1^B2
print(B1) # B1的內容沒有改變
print(B3) # B3的內容是對稱差集的結果
B1.symmetric_difference_update(B2) # 將B1和B2進行對稱差集的結果更新到B1
print(B1) # B1的內容更新成對稱差集的結果