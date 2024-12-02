import re
import numpy as np

file_path = "../data/d1.in"

with open(file_path, "r") as f:
    # Parsing
    data = np.array([list(map(int, re.findall(r"\d+", line))) for line in f]).T

    # Parte 1
    print(np.sum(np.abs(np.sort(data[0]) - np.sort(data[1]))))

    # Parte 2
    print(sum(x * data[1].tolist().count(x) for x in data[0]))

        