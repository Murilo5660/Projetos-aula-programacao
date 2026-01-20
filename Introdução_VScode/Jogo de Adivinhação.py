import random
palpite = 0
numero_secreto = random.randint(1,100)

while palpite != numero_secreto:

    palpite = int (input("De um palpide de qual número estou pensando: "))

    if palpite < numero_secreto:
        print ("É maior! ")
    elif palpite > numero_secreto:
        print ("É menor! ")
    else:
        print ("Parabéns! ")
