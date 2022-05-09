print(format(123,"<10")) # align 設定欄位寬度與對齊方式(數值預設為靠右)
# 欄位設定為10字元，靠左
print(format(123,">10"))
# 欄位設定為10字元，靠右
print(format(123,"^10"))
# 欄位設定為10字元，置中
print(format(123,"$^10"))
# 欄位設定為10字元，置中，以$填滿空位

print(format(12345678,",")) # , 設定加上千分位符號

print(format(65,"#b")) # #設定二、八、十六進位表示法並加上0b、0o或0x
print(format(65,"#o"))
print(format(65,"#x"))

print(format(123,"=+010")) # 0 設定加上正負符號並在正負符號和數字之間的空位填滿0
