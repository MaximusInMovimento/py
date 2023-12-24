test_txt_orig = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
print(test_txt_orig)

test_txt = test_txt_orig.lower()

with open('input4.txt') as f:
    badline = f.readline()
    blacklist = badline.split()

    for word in blacklist:
        patch = ""
        for a in word:
            patch += '*'
        test_txt = test_txt.replace(word, patch)

new_txt = ""
for idx in range(len(test_txt_orig)):
    letter = test_txt[idx]
    if letter != '*':
        letter = test_txt_orig[idx]
    new_txt += letter

print(new_txt)
