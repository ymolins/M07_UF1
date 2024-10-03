paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

if len(paraula1) >= 2 and len(paraula2) >= 2:
    nova_paraula1 = paraula2[:2] + paraula1[2:]
    nova_paraula2 = paraula1[:2] + paraula2[2:]

    print(f"Resultat: {nova_paraula1} {nova_paraula2}")
else:
    print("Les dues paraules han de tenir almenys 2 caràcters.")
