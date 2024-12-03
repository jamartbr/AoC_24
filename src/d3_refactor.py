import re

file_path = "../data/d3.in"
with open(file_path, "r") as f:
    suma1, suma2 = 0, 0
    active = True

    for x, y, do_not, do in re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(don't)|(do)", f.read()):
        if x:
            aux = int(x) * int(y)
            suma1 += aux
            suma2 += aux * active
        else:
            active = True if do else False

    print(suma1, suma2)