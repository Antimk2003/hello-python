A = [[1,2],
    [5,6]]
B = [[0,5],
    [1,7]]    

Final = [[0,0],
        [0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        Final[i][j] = A[i][j] + B[i][j] 
for r in Final:
    print(r)               