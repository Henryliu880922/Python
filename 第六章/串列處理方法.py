'''
list.append 將參數所指定的元素加入串列的尾端
list.extend 將參數所指定之串列的所有元素加入串列
list.insert 將參數所指定的元素插入串列中索引為參數的位置
list.remove 從串列中刪除第一個值為參數的元素
list.pop 從串列中刪除索引為選擇性參數的元素並傳回該元素，若沒有指定參數，就刪除最後一個元素並傳回該元素
'''

list1=[10,20,30,40,50]
list2=[100,200,300]
list1.append(60) # 將60加入串列的尾端
print(list1)
list1.extend(list2) #將list2串列加入list1串列
list1.insert(1,1000) #將1000插入索引為1的位置
print(list1)
list1.remove(1000) #刪除第一個值為1000的元素
print(list1)
list1.pop() #刪除最後一個元素並傳回該元素
print(list1)

'''
list.index 傳回參數所指定的元素第一次出現在串列的索引
list.count 傳回參數所指定的元素出現在串列中的次數
list.sort 將串列中的元素由大到小排序
list.reverse 將串列中的元素順序反轉過來
list.copy 傳回串列的副本，這和原來的串列是不同的物件
list.clear 從串列中刪除所有元素
'''

list3=[50,20,40,20,30,20,10]
print(list3.index(20))
print(list3.count(20))
list3.sort()
print(list3)
list3.reverse()
print(list3)
list4=list3.copy()
print(list3)
list4.clear()
print(list4)