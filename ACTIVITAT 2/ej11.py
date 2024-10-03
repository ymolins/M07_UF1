import random

numero_secret = random.randint(1, 100)
intents = 0
encertat = False

print("Endevina el número entre 1 i 100!")

while not encertat:
    intent = int(input("Posa un número: "))
    intents += 1

    if intent < numero_secret:
        print("El número és més gran.")
    elif intent > numero_secret:
        print("El número és més petit.")
    else:
        print(f"Felicitats! Has encertat el número {numero_secret} en {intents} intents.")
        encertat = True
