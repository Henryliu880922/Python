# 逸脫序列

print("\"Python\"程式設計") # 使用逸脫序列\"顯示雙引號(")
print("\"101") # 八進位整數101表示字母A (ASCII碼為65)
print("\"x41") # 十六進位整數41表示字母A
print("\u0041") # Unicode \u0041 表示字母A
print("\N{Black SPADE SUIT}") # 字元名稱Black SPADE SUIT表示黑桃

# 內建字串函式
# ord 傳回字元參數的Unicode碼(十進位)
print(ord('A'))
print(ord('€'))

# chr 傳回整數參數所表示的Unicode字元
print(chr(65))
print(chr(8364))

# len 傳回字串參數的長度，就是字串是由幾個字元所組成
print(len("Python程式設計"))

# max 傳回字串參數中Unicode碼最大的字元
print(max("Python程式設計"))

# min 傳回數值參數中Unicode碼最小的字元
print(min("Python程式設計"))

# str 傳回數值參數轉換成字串的結果
print(str(-123.8))

# 連接運算子 可以用來連接字串
print("Happy "+" Birthday"+" To"+" 小美")

#重複運算子 也可以用來連結字串
print(3*"Oh！")

# 比較運算子
print('我'>'A')
print('1'>'A')
print('abc'=='ABC')
print('abcd'=='ABCd')

# in 與 not in 運算子 檢查某個字串是否存在、不存在於另一個字串
print("or" in "forever")
print("or"not in "forever")

# 索引與片段運算子

# 片段運算子
s="Python程式設計"
print(s[2:5])
print(s[3:7])
print(s[6:-1])

#索引運算子
print(s[:2]) # 省略第一個索引值表示採取預設值為0
print(s[2:]) # 指定索引範圍時省略第二個索引表示採取預設值為字串的長度