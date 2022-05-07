import time

print(time.time()) # 傳回從1970/1/1上午12時0分到目前的UTC時間總共經過多少秒

print(time.gmtime()) # 傳回從1970/1/1上午12時0分經過time.time()或選擇性參數所指定之秒數的時間，即目前的UTC時間
# 傳回目前的UTC時間

print(time.localtime()) # 用途和time.gmttime函式類似，但傳回的是目前本地時間，以台灣為例，傳回的tm_hour屬性會比UTC時間快8小時
# 傳回目前的本地時間

print(time.asctime()) # 以str型別傳回目前的本地時間或選擇性參數指定的時間 
# 傳回目前的本地時間
print(time.asctime((2016,12,8,12,17,30,3,343,0)))
# 傳回參數指定的時間

print(time.ctime()) # 用途和time.asctime函式相同，但是從1970/1/1上午12時0分所經過的秒數
# 傳回目前的本地時間
print(time.ctime(1481170650.0))
# 傳回參數指定的時間

print(time.mktime((2016,12,8,12,17,30,3,343,0))) # 傳回從1970/1/1上午12時0分到參數指定的時間所經過的秒數

print(time.sleep(1)) # 令Python暫停參數所指定的秒數

# time.strftime()根據參數所指定的格式，將time.gmttime()或time.localtime()函式傳回的幕前時間轉換成字串，格式化符號如日期與時間函式.md所示，若要指定愈進行格式化時間，可以使用選擇性參數指定時間
print(time.strftime("%Y 年 %m 月%d 日 %H:%M:%S%Z"))
print(time.strftime("%Y 年%m 月%d 日"))
print(time.strftime("%H:%M:%S"))
t=(2016,12,15,11,2,9,3,350,0)
print(time.strftime("%a,%d %b %Y %H:%M:%S",t))

# time.strptime()根據參數所指定的格式，將參數所指定的字串剖析成time.struct_time，相當於time.strftime()的反函式
print(time.strptime("30 Nov 00","%d %b %y"))
