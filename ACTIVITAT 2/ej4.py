valor1 = float(input("Introdueix el primer valor: "))
valor2 = float(input("Introdueix el segon valor: "))

suma = valor1 + valor2
resta = valor1 - valor2
multiplicacio = valor1 * valor2
divisio = valor1 / valor2 if valor2 != 0 else "Indefinit (no es pot dividir per zero)"

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicació: {multiplicacio}")
print(f"Divisió: {divisio}")
