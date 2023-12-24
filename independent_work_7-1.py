import re

words_q = {}
words = []

with open('article.txt') as f:
    lines = f.readlines()
    for line in lines:
        for word in line.split():
            w = word.lower()
            w = re.sub(r'[,.!?\'\"]$', '', w)
            w = re.sub(r'^[\'\"]', '', w)
            words.append(w)

for word in words:
    words_q.update({word: words.count(word)})

frequent = sorted(words_q.items(), key=lambda x: -x[1])

print(f"Всего слов в статье: {len(words)}\nСамое часто встречающееся слово - \"{frequent[0][0]}\" ({frequent[0][1]} раз)")
