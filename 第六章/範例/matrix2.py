matrix=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
def printMatrix(matrix): # 定義printMatrix()方法來印出矩陣
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                print(matrix[i][j],'\t',end=' ')
        print('\n')
printMatrix(matrix) # 呼叫printMatrix()方法印出矩陣