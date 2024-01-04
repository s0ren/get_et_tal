import random

tal = random.randint(1, 100)

# print(tal)

while True:
    gæt = int(input("Hvad gætter du på? "))
    # print(gæt)
    if gæt == tal:
        print("Ja, tallet er", gæt)
        break
    elif tal < gæt:
        print("Tallet er lavere end", gæt)
    else:
        print("Tallet er højere end", gæt)
