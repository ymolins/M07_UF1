paraules = input("Introdueix entre 1 i 3 paraules: ")

paraules_split = paraules.split()

if 1 <= len(paraules_split) <= 3:
    for paraula in paraules_split:
        longitud = len(paraula)
        primer_caracter = paraula[0]
        ultim_caracter = paraula[-1]
        print(f"Paraula: {paraula}, Longitud: {longitud}, Primer caràcter: {primer_caracter}, Últim caràcter: {ultim_caracter}")
else:
    print("Has d'introduir entre 1 i 3 paraules.")
