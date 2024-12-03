file_path = "../data/d2.in"

with open(file_path, "r") as f:
    data = [[int(x) for x in line.split()] for line in f]

def check_line(line):
    diff = [line[i]-line[i+1] for i in range(len(line)-1)]
    return ((min(diff)<0 and max(diff)<0) or (min(diff)>0 and max(diff)>0)) and all([abs(x) in (1, 2, 3) for x in diff])

suma1, suma2 = 0, 0
for line in data:
    # Parte 1
    suma1 += check_line(line)
    # Parte 2
    suma2 += any([check_line(line[:i]+line[i+1:]) for i in range(len(line))])

print(suma1, suma2)
