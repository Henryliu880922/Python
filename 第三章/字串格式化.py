# 設定字串的欄位寬度與對齊方式(字串預設為靠左)
print(format("Hello,World！","20")) # 欄位寬度為20字元，預設為靠左
print(format("Hello,World！",">20")) # 欄位寬度為20字元，靠右
print(format("Hello,World！","^20")) # 欄位寬度為20字元，置中
print(format("Hello,World！","10")) # 若字串長度超過欄位寬度，寬度會自動增加
