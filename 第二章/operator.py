#加法
print(12+3)
print(1.234+5.678)

#減法
print(12-3)
print(1.234-5.678)

#乘法
print(12*3)
print(10*0.5)

#浮點數除法
print(12/3)
print(7/3)

#整數除法
print(12//3)
print(7//3)

#餘數
print(12%5)
print(12.5%5)

#指數
print(9**2)
print(9**0.5)

#移位運算子
#<< 為向左移位
#>> 為向右移位

print(1<<3)
print(3>>1)

#位元運算子(可以以後再來研究)
#NOT
print(~1)
#AND
print(10&6)
#OR
print(10|6)
#XOR
print(10^6)

#比較運算子 否會傳回False 是會傳回True
a=1
b=2
print(a<b) #小於
print(a>b) #大於
print(a<=b)#小於等於
print(a>=b)#大於等於
print(a==b)#等於
print(a!=b)#不等於
#指派運算子
c,d,e=1,2,3
f,g=0,3
c=e#將c的值指派給e
print(c)
c+=e#c=c+e 相當於c=c+e
print(c)
c-=e#c=c-e 相當於c=c-e
print(c)
c*=e#c=c*e 相當於c=c*e
print(c)
c/=e#c=c/e 相當於c=c/e 浮點數除法
print(c)
c//=e#c=c//e 相當於c=c//e 整數除法
print(c)
c%=e#c=c%e 相當於c=c%e 餘數
print(c)
c**=e#c=c**e 相當於c=c**e 指數
print(c)

f<<=g#f=f<<g 相當於f=f<<g 向左移位
print(f)
g>>=f#g=g>>f 相當於g=>>f 向左移位
print(g)
f&=g#f=f&g 相當於c=c&e AND運算
print(f)
f|=g#f=f|g 相當於f=f|g OR運算
print(f)
f^=g#f=f^g 相當於f=f^g XOR運算
print(f)

#邏輯運算子 and
print(5>4 and 3>2) #5大於4為True，3大於2為True，True and True會得到True
print(5>4 and 3<2) #5大於4為True，3小於2為False，True and False會得到False
print(5<4 and 3>2) #5小於4為False，3大於2為True，False and True會得到False

#邏輯運算子 or
print(5>4 or 3<2) #5大於4為True，3小於2為False，True or False會得到True
print(5<4 or 3>2) #5小於4為False，3大於2為True，False or True會得到True
print(5<4 or 3<2) #5小於4為False，3小於2為False，False or False會得到False

#邏輯運算子 not
print(not 5>4) #5大於4為True，not True會得到False
print(not 5<4) #5小於4為False，not False會得到True