print(str.isalpha("5apple")) # str.isalpha 若字串參數的所有字母都是英文，就傳回True，反之則傳回False
print(str.isalpha("Happy"))

print(str.isdigit("213")) # str.isdigit 若字串參數的所有字元都是數字，就傳回True，反之則傳回False
print(str.isdigit("5apple"))

print(str.isalnum("123.45")) # 若字串參數的所有字元都是英文或數字，就傳回True，反之則傳回False
#小數點不是英文或數字
print(str.isalnum("5apple"))

print(str.isupper("Happy")) # 若字串參數的所有字元都是大寫的英文，就傳回True，反之則傳回False
print(str.isupper("HAPPY"))

print(str.islower("Happy")) # 若字串參數的所有字元都是小寫的英文，就傳回True，反之則傳回False
print(str.islower("happy"))

print(str.isidentifier("happy")) # 若字串參數是合法的識別字，就傳回True，反之則傳回False。若要測試字串參數是否為關鍵字，可以用keyword.iskeyword函式
print(str.isidentifier("5apple"))
print(str.isidentifier("class"))
import keyword
print(keyword.iskeyword("None"))

print(str.isspace("  ")) # 若字串參數的所有字元都是空白，就傳回True，反之則傳回False

print(str.istitle("Happy New Year")) # 若字串參數的每個單字的第一個字元都是大寫英文字母，就傳回True，反之則傳回False
