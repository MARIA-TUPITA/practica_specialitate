import csv

def ghiceste_cuvant(cuvant_start, cuvant_target):
    cuvant_curent = list(cuvant_start)
    incercari = 0

    for i in range(len(cuvant_target)):
        for j in range(len(cuvant_target)):
            if i == j:
                if cuvant_curent[i] == "*":
                    cuvant_curent[i] = cuvant_target[i]
                    incercari += 1
                else:
                    incercari += 1

    return "".join(cuvant_curent), incercari

# Funcție principală care citește fișierul și aplică procesul
def automatizare(fisier):
    total_incercari = 0
    cuvinte_ghicite = 0
    max_incercari = 1200  # Limita de încercări

    # Deschidem fișierul CSV
    with open(fisier, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for linie in reader:
            cod_joc = linie[0]
            cuvant_start = linie[1]  # Cuvântul de pornire
            cuvant_target = linie[2]  # Cuvântul final de ghicit

            # Ghicim cuvântul
            cuvant_final, incercari = ghiceste_cuvant(cuvant_start, cuvant_target)

            if incercari > 0:
                total_incercari += incercari
            else:
                total_incercari += 1

            cuvinte_ghicite += 1

            if total_incercari > max_incercari:
                print(f"Am depășit limita de {max_incercari} încercări.")
                break

            print(f"Cuvântul de pornire: {cuvant_start}, cuvântul ghicit: {cuvant_final}, încercări: {incercari}")

    # Rezultatul final
    print(f"\nRezultatul final:")
    print(f"Cuvinte ghicite: {cuvinte_ghicite}")
    print(f"Încercări totale: {total_incercari} (din {max_incercari} posibile)")

# Apelăm funcția principală cu fișierul CSV dat
automatizare('cuvinte_de_verificat.txt')
