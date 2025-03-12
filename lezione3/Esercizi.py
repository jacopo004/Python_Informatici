#ESERCIZIO 1
mioNome = "Jacopo"
mioCognome = "Pisano"
print("Il mio nome è", mioNome, "e il mio cognome è", mioCognome)


#ESERCIZIO2
baseRettangolo = 5.7
altezzaRettangolo = 6.2

perimetroRettangolo = (baseRettangolo * 2) + (altezzaRettangolo * 2)
print("Il perimetro vale:", perimetroRettangolo)

areaRettangolo = baseRettangolo * altezzaRettangolo
print("L'area vale:", areaRettangolo)


#ESERCIZIO3
lato1Triangolo = 9
lato2Triangolo = 12
lato3Triangolo = 15

perimetroTriangolo = lato1Triangolo + lato2Triangolo + lato3Triangolo
print("Il perimetro del triangolo è:", perimetroTriangolo)

p1 = (lato1Triangolo ** 2) / lato3Triangolo
print("risultato =", p1)
p2 = lato3Triangolo - p1
print(p2)

hTriangolo = ((lato1Triangolo **2) + (p1 ** 2)) **(1/2)
print(hTriangolo)

areaTriangolo = (lato3Triangolo * hTriangolo) / 2
print("L'area del triangolo è:", areaTriangolo)