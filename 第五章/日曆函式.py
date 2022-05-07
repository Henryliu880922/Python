import calendar

# calendar.firstweekday 傳回一週的第一個工作天，預設值為0表示星期一
# calendar.setfirstweekday() 將一週的第一個工作天設定為參數所指定的日子，0~6表示星期一到星期日
print(calendar.firstweekday()) # 傳回0表示第一個工作天是星期一
print(calendar.setfirstweekday(1)) # 將第一個工作天設定為星期二
print(calendar.firstweekday()) #傳回1表示第一個工作天是星期二

# calendar.isleap() 若參數所指定的年份是閏年，就傳回True，反之則傳回False
print(calendar.isleap(2000)) # 傳回True表示2000年是閏年
print(calendar.isleap(2001)) # 傳回False表示2001年不是閏年

# calendar.weekday() 傳回參數所指定的年月日是星期幾，0~6表示星期一~星期日
print(calendar.weekday(2016,12,9)) # 傳回4表示2016年12月9日是星期五

# calendar.monthrange() 傳回兩個整數，第一個整數表示年月的第一天是星期幾，第二個整數表示該月份有幾天
print(calendar.monthrange(2016,12))# 傳回2016年12月第一天是星期四，有31天

# calandar.calandar() 傳回參數所指定之年份月曆
print(calendar.calendar(2022))

# calandar.month() 傳回參數所指定之年份與月份的日曆
print(calendar.month(2022,5))