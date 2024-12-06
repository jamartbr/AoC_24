def mov(data):
    visitadas = set()
    pos = min(x for x in data if data[x] == '^')
    dir = -1
    while pos in data and (pos,dir) not in visitadas:
        visitadas.add((pos,dir))
        if data.get(pos+dir) == "#":
            dir *= -1j
        else: pos += dir
    return visitadas, (pos,dir) in visitadas

file_path = "../data/d6.in"
with open(file_path, "r") as f:
    data = {index_fila+index_col*1j: char for index_fila,fila in enumerate(f) for index_col,char in enumerate(fila.strip())}

camino, es_bucle = mov(data)
casillas = {pos for pos,dir in camino}

bucles = 0
for pos in casillas:
    if data[pos] == '.':
        data[pos] = "#"
        bucles += mov(data)[1]
        data[pos] = '.'

print(len(casillas),bucles)

            