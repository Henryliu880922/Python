def CtoF2(degreeC):
    degreeF=degreeC*1.8+32
    return degreeF

temperatureC=eval(input("請輸入攝氏溫度："))
temperatureF=CtoF2(temperatureC) # 呼叫函式並傳遞攝氏溫度做為參數
print("攝氏",temperatureC,"度可以轉換成華氏",temperatureF,"度")