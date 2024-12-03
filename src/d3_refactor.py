import re

file_path = "../data/d3.in"
with open(file_path, "r") as f:
    data = f.readlines()

    # Parte 1
    print(sum(int(x[0]) * int(x[1]) for linea in data for x in re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", linea)))
    
    # Parte 2
    suma = 0
    active = True
    for linea in data:
        data = re.split(r"don't", linea)    # Primero dividimos por "don't" -> i++ implica desactivar
        data = [re.split(r"do", x) for x in data] # Luego dividimos por "do" -> j++ implica activar
        for i in range(len(data)):
            if i!=0:
                active = False
            for j in range(len(data[i])):
                if j!=0:
                    active = True
                if active:
                    aux = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", data[i][j])
                    for x in aux:
                        suma += int(x[0]) * int(x[1])
    print(suma)
    