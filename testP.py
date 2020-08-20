col, row = map(int, input().split())
matrix = []
answer = [[0] * col for i in range(row)]
for i in range(row):
    matrix.append(list(input()))

for i in range(row):
    for j in range(col):
        if(matrix[i][j] == '*'):
            if(i - 1 >= 0):
                if(j - 1 >= 0):
                    answer[i-1][j-1] = answer[i-1][j-1] + 1
                if(j + 1 < col):
                    answer[i-1][j+1] = answer[i-1][j+1] + 1
                
                answer[i-1][j] = answer[i-1][j] + 1
            if(i + 1 < row):
                if(j - 1 >= 0):
                    answer[i+1][j-1] = answer[i+1][j-1] + 1
                if(j + 1 < col):
                    answer[i+1][j+1] = answer[i+1][j+1] + 1
                
                answer[i+1][j] = answer[i+1][j] + 1
            
            if(j - 1 >= 0):
                answer[i][j-1] = answer[i][j-1] + 1
            if(j + 1 < col):
                answer[i][j+1] = answer[i][j+1] + 1

for i in range(row):
    for j in range(col):
        if(matrix[i][j] == '*'):
            print('*', end='')
        else:
            print(answer[i][j], end='')
    print()
