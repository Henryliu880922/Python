list1=[i for i in range(10)] # 串列的元素是for敘述的i
print(list1)
list2=[j*2 for j in range(10)] # 串列的元素是for敘述的j乘以2
print(list2)
list3=[k for k in range(10) if k<8] # 串列的元素是for敘述的k且k要小於8
print(list3)
list4=[-1.5,-2,0,2,8]
list5=[abs(a)for a in list4] #串列的元素是list4串列中每個元素的絕對值
print(list5)
list6=[b for b in list4 if b>=0] # 串列的元素是list4串列中大於0的元素
print(list6)
list7=[c**2 for c in list4] # 串列的元素是list4串列中每個元素的平方
print(list7) 