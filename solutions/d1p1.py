import re
import numpy as np

file_path = "../data/d1.in"
with open(file_path, "r") as f:
    data = [(int(x), int(y)) for x, y in [re.search(r"([0-9]*) *([0-9]*)", linea).groups() for linea in f.readlines()]]
    data = np.array([[x[0], x[1]] for x in data]).T
    data = np.sort(data)
    print(np.sum(np.abs(data[0] - data[1])))

        