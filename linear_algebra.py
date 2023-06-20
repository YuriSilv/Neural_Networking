def transposta(a: list):
    c = []
    for i in range(len(a[0])):
        c.append([])
        for j in range(len(a)):
            c[i].append(a[j][i])
    return c    
            

def matriz_sum(a: list, b: list, isSub = False):
    matriz = []
    for row in range(len(b)):
        matriz.append([])
        for col in range(len(b[0])):
            if(isSub):
                matriz[row].append(a[row][col] - b[row][col])
                continue
            matriz[row].append(a[row][col] + b[row][col])
    
    return matriz

def matriz_multi_scalar(a: list, y: float):
    matriz = []
    for row in range(len(a)):
        matriz.append([])
        for col in range(len(a[0])):
            matriz[row].append(a[row][col] * y)

    return matriz

def matriz_multi(a: list, b: list, round_factor: int = 3):
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        raise Exception("Matrizes não podem ser multiplicadas")

    matriz = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += round(a[i][k] * b[k][j], round_factor)
            matriz[i][j] = total

    return matriz

def acceptable_matrix(a: list, limit_upper: float = 0.1, limit_lower: float = -0.1):
    for i in range(len(a)):
        for j in range(len(a[0])):

            if(a[i][j] >= limit_lower and a[i][j] <= limit_upper):
                continue
            else:
                return False
            
    return True
    