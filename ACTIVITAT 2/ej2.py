valor = float(input("Introdueix el valor en €: "))

while True:
    iva = float(input("Introdueix el % d'IVA (4, 10 o 21): "))
    if iva in [4, 10, 21]:
        break
    print("L'IVA ha de ser 4, 10 o 21")

iva_aplicat = valor * (iva / 100)
valor_final = valor + iva_aplicat

print(f"Valor inicial: {valor}€")
print(f"IVA aplicat: {iva}%")
print(f"Valor final amb IVA: {valor_final}€")
