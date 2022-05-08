from cmd import PROMPT

list1=[] #串列變數list1用來存放5位評審給某位選手的分數，初始值位空串列

for i in range(1,6): # 使用For迴圈要求輸入分數，然後呼叫append方法將分數加入串列的尾端
    PROMPT="請輸入第"+str(i)+"位評審的分數："
    score=eval(input(PROMPT))
    list1.append(score)

print("這位選手的總分為",sum(list1)) # 呼叫sum方法計算總分，並印出結果