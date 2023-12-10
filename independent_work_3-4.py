import re
text = str(input("Введите предложение на англ. языке: "))
print("Длина предложения", len(text))
print("Предложение в нижнем регистре", text.lower())
print("Количество строчных букв `a`: ", text.count('a'))
print("Количество строчных букв `e`: ", text.count('e'))
print("Количество строчных букв `i`: ", text.count('i'))
print("Количество строчных букв `o`: ", text.count('o'))
print("Количество строчных букв `u`: ", text.count('u'))
print("Предложение с заменой `ugly` на `beauty` `u`: ", text.replace('ugly', 'beauty'))
if bool(re.search('^The', text)):
    print("Предложение начинается на `The`")
if bool(re.search('end$', text)):
    print("Предложение заканчивается на `end`")
