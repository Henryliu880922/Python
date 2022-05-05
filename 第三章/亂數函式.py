"""
亂數函式
random.randint 傳回一個大於等於整數整數參數X、小於等於整數參數Y的隨機整數，每次亂數呼教所傳回的亂數不一定相同
random.random 傳回一個大於等於0.0、小於1.0的隨機浮點數，每次亂數呼教所傳回的亂數不一定相同
random.shuffle 將參數X中的元素隨機重排
"""
import random
print(random.randint(1,10))
print(random.random())
print(random.random())
L=[1,2,3,4,5]
print(random.shuffle(L))