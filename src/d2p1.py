import re
import numpy as np

file_path = "../data/d2.in"
with open(file_path, "r") as f:
    data = [x.split() for x in f.readlines()]
    data = [[int(x) for x in y] for y in data]
    suma = 0
    for line in data:
        safe = True
        sube = line[0] < line[1]
        for i in range(len(line)-1):
            diff = abs(line[i]-line[i+1])
            if diff<1 or diff>3:
                safe = False
                break
            if (sube and line[i]>line[i+1]) or (not sube and line[i]<line[i+1]):
                safe = False
                break
        if safe:
            suma+=1
print(suma)

        