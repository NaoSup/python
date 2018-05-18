matrice = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

def matrice_trans(m):
    transposed = [
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    for i in range(len(m)):
         for j in range(len(m[i])):
            transposed[j][i] = m[i][j]
    return transposed


transposed2 = [[row[i] for row in matrice] for i in range(5)]
    

print(matrice_trans(matrice))
print(transposed2)

x=[1,2,3]
y=[4,5,6]
print(list(zip(x,y)))

print(list(zip(*matrice)));
