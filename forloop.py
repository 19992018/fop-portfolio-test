import random

scores = [19, 64, 74, 49, 32, 29]
for i in range(len(scores)):
    def generaterandomid():
        randomid = random.randint(100000,999999)
        return str(randomid)
for score in scores:
    randomid = generaterandomid()
    print(score, randomid)

