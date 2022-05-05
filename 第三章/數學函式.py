# 數學函式

from cmath import nan
import math

# math.pi、math.e、math.nan、math.inf 表示圓周率、自然對數的底數e、NaN(not a number)、正無限大，而負無限大為 math.inf
print(math.pi)
print(math.e)

# math.celi 傳回比數值參數X大1的整數 
print(math.ceil(9.999))
print(math.ceil(-9.999))

# math.fabs 傳回數值參數X的浮點數絕對值
print(math.fabs(-5))

# math.factorial 傳回正整數參數X的階乘值
print(math.factorial(5))

# math.floor 傳回比數值參數X小1的整數
print(math.floor(4.3))
print(math.floor(-4.3))

# math.gcd 傳回整數參數X與整數參數Y的最大公因數
print(math.gcd(25,155))

# math.exp 傳回自然對數之底數e的數值參數X次方值
print(math.exp(2))

# math.log 傳回正數值參數X的自然對數值，預設的底數為e，若要設定底數，可以加上選擇性參數base
print(math.log(2))
print(math.log(2,2))

# math.sqrt 傳回正數值參數X的平方根
print(math.sqrt(2))

# math.isfinite 傳回數值參數X是否為有限
print(math.isfinite(1000000))

# math.isinf 傳回數值參數X是否為無限
print(math.isinf(-math.inf))

# math.isnan 傳回數值參數X是否為NaN(not a number)
print(math.isnan(math.nan))

# math.radians 傳回數值參數X由角度轉換成弳度的結果
print(math.radians(45))

# math.degrees 傳回數值參數X由弳度轉換為角度的結果
print(math.degrees(0.7853981633974483))

# math.cos、math.sin、math.tan、math.acos、math.sin、math.atan 三角函式 傳回數值參數X的餘弦值(consine)、正弦值(sine)、正切值(tangent)、反餘弦值(arccosine)、反正弦值(arcsine)、反正切值(arctangent) 參數X必須為弳度，而不是角度。若要計算sin30°和cos30°的值，必須先將角度轉換成弳度
print(math.sin(30*math.pi/180))
print(math.cos(30*math.pi/180))
