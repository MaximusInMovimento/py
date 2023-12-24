import re

w = []
chars = 0
with open('input3.txt') as f:
    lines = f.readlines()
    for line in lines:
        for word in line.split():
            w.append(word)
            weng = re.sub(r'[^a-zA-Z]*', '', word)
            chars += len(weng)

    print(f"{chars} letters")
    print(f"{len(w)} words")
    print(f"{len(lines)} lines")
