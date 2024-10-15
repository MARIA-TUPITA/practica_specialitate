import csv

# Funcție care încearcă să completeze cuvântul ghicit
def ghiceste_cuvant(cuvant_start, cuvant_target):
    incercari = 0
    cuvant_curent = list(cuvant_start)
    cuvant_target = list(cuvant_target)

    # Parcurgem fiecare literă din cuvântul țintă
    for i in range(len(cuvant_target)):
        if cuvant_curent[i] == "*":
            cuvant_curent[i] = cuvant_target[i]
            incercari += 1  # Numărăm fiecare încercare de ghicire a unei litere

    return "".join(cuvant_curent), incercari

# Funcție principală care citește fișierul CSV și aplică procesul de ghicire
def automatizare_identificare(fisier):
    total_incercari = 0
    cuvinte_ghicite = 0
    max_incercari = 1200  # Limita de încercări

    with open(fisier, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for linie in reader:
            cod_joc = linie[0]
            cuvant_start = linie[1]
            cuvant_target = linie[2]

            # Ghicim cuvântul
            cuvant_final, incercari = ghiceste_cuvant(cuvant_start, cuvant_target)
            total_incercari += incercari
            cuvinte_ghicite += 1

            # Verificăm dacă am depășit limita de încercări
            if total_incercari > max_incercari:
                print(f"Am depășit limita de {max_incercari} încercări.")
                break

            print(f"Cuvântul de pornire: {cuvant_start}, cuvântul ghicit: {cuvant_final}, încercări: {incercari}")

    print(f"\nRezultatul final:")
    print(f"Cuvinte ghicite: {cuvinte_ghicite}")
    print(f"Încercări totale: {total_incercari} (din {max_incercari} posibile)")

# Apelăm funcția principală cu fișierul CSV dat
automatizare_identificare('cuvinte_de_verificat.txt')


