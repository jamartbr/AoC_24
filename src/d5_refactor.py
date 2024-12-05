import functools

file_path = "../data/d5.in"
with open(file_path, "r") as f:
    rules, pages = [x.split() for x in f.read().split("\n\n")]
    rules = [list(map(int, rule.split("|"))) for rule in rules]
    pages = [list(map(int, page.split(","))) for page in pages]

wrong = []
for rule in rules:
    for line in pages:
        if all(x in line for x in rule) and line.index(rule[0]) > line.index(rule[1]):
            wrong.append(line)
            pages.remove(line)

def order(x, y):
    for a,b in rules:
        if a==x and b==y:
            return -1
        elif a==y and b==x:
            return 1
    return 0

wrong = [sorted(line, key=functools.cmp_to_key(order)) for line in wrong]

print(sum([line[len(line)//2] for line in pages]), sum([line[len(line)//2] for line in wrong]))