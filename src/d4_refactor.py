def check_XMAS(data, i, j):
    directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
    out = 0
    for dir in directions:
        x, y = i, j
        for char in "MAS":
            x += dir[0]
            y += dir[1]
            if not (0 <= x < len(data) and 0<= y < len(data[0]) and data[x][y] == char):
                break
        else:
            out += 1
    return out

def check_X_MAS(data, i, j):
    directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
    for dir in directions:
        if data[i+dir[0]][j+dir[1]] == 'M' and data[i-dir[0]][j-dir[1]] == 'S':
            aux = (data[i+dir[0]][j-dir[1]], data[i-dir[0]][j+dir[1]])
            if 'S' in aux and 'M' in aux:
                return True
    return False


file_path = "../data/d4.in"
with open(file_path, "r") as f:
    data = [list(x.rstrip()) for x in f.readlines()]
    suma_1 = suma_2 = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'X':
                suma_1 += check_XMAS(data, i, j)
            elif 0<i<len(data)-1 and 0<j<len(data[0])-1 and data[i][j] == 'A':
                suma_2 += check_X_MAS(data, i, j)
    print(suma_1, suma_2)