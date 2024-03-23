from random import randint
final =""
for i in range(80):
    word = list("It just tak3s pract!ce")
    for _ in range(1,len(word)):
        rand = randint(0,len(word)-1)
        final += word.pop(rand)
    final += "~~"
print(final)
