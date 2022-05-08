print([1,"Taipei",2,"Tokyo"]) # 包含4個元素的串列
print([2,"Taipei",1,"Tokyo"]) # 元素相同但順序不同，表示不同串列

list1=list() # 建立空串列
print(list1)
list2=list([1,2,3]) # 建立包含1,2,3的串列
print(list2)

list3=[]
list4=[1,2,3]
print(list3,list4)

list5=list("ABCA") # 從字串建立包含'A','B','C','A'的串列
print(list5)
list6=list(range(5)) # 從range物件建立包含0,1,2,3,4的串列
print(list6)
list7=list(range(10,0,-2)) # 從range物件建立包含10,8,6,4,2的串列
print(list7)

print("1 2 3".split()) # 根據空白將字串分隔成串列
print("1,2,,3".split(',')) # 根據逗號將字串分隔成串列