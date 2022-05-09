add=lambda x,y:x+y
print(add(1,2))
print(add(50,-100))
print(add(50,3.8))
print(add(50,True)) # True會被當成數值1
print(add(50,False)) # False會被當成數值0
print(add("abc","de"))