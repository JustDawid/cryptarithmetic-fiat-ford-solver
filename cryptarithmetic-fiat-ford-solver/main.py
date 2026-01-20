from itertools import permutations

def rozwiaz_algebraf():
    cyfry = range(1, 9)
    rozwiazania = []

    for perm in permutations(cyfry, 8):
        F, I, A, T, O, R, U, D = perm

        if R != 2 * I:
            continue
        
        FIAT = 1000 * F + 100 * I + 10 * A + T
        FORD = 1000 * F + 100 * O + 10 * R + D
        AUTA = 1000 * A + 100 * U + 10 * T + A
        
        if FIAT + FORD == AUTA:
            rozwiazania.append({
                "F": F, "I": I, "A": A, "T": T,
                "O": O, "R": R, "U": U, "D": D
            })
    
    return rozwiazania if rozwiazania else "Brak rozwiązania"

wyniki = rozwiaz_algebraf()
print("Rozwiązania algebrafu:", wyniki)

if wyniki != "Brak rozwiązania":
    wartosci_szukane = [7, 1, 2, 4]
    wynik = "".join(
        klucz
        for wartosc in wartosci_szukane
        for klucz, val in wyniki[0].items() if val == wartosc
    )
    print(wynik)
else:
    print("Brak rozwiązania")