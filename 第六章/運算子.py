print([1,2,3]+["Taipei","Tokyo","Vienna"]) # 連接運算子

print(3*[1,2,3]) # 重複運算子
print([1,2,3]*3)

print([1,"神隱少女","宮崎駿"]==["神隱少女","宮崎駿",1]) # 比較運算子
print([1,2,3]!=[1,2,3,4])
print(['a','b','c','d','e']>['a','b','c','d','E'])
print(['我','是','A']<['我','是','B'])

print("Taipei" in [1,"Taipei",2,"Tokyo"]) # in與 not in運算子
print("Vienna" in [1,"Taipei",2,"Tokyo"])
print("Taipei" not in [1,"Taipei",2,"Tokyo"]) 
print("Vienna" not in [1,"Taipei",2,"Tokyo"])

L=[5,10,15,20,25,30,35,40,45,50]
print(L[2:5])
print(L[3:7])
print(L[6:-1])
print(L[:2]) # 索引0到1的元素(不含索引2)
print(L[2:]) # 索引2到9的元素(不含索引10)

sum=0
for i in L:
    sum=sum+i
print(sum)
