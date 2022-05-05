print("Hello,World！".center(20)) # str.center 傳回欄位寬度為參數所指定的字元數、置中的字串
# 傳回欄位寬度為20、置中的字串
print("Hello,World！".ljust(20)) # str.ljust 傳回欄位寬度為參數所指定的字元數、靠左的字串
# 傳回欄位寬度為20、置左的字串
print("Hello,World！".rjust(20)) # str.rjust 傳回欄位寬度為參數所指定的字元數、靠右的字串
# 傳回欄位寬度為20、置右的字串

print("-42".zfill(5)) # str.zfill 傳回欄位寬度為參數所指定的字元數、左側填上0、正負符號保留在開頭的字串

# str.format 根據參數所指定的格式將字串格式化，然後傳回結果，這方法和內建的format()函式類似