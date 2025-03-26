# OR logico. In questo caso vale una condizione OPPURE l'altra affinchè quella globale sia true

#esami: l'esame viene superato se passi lo scritto oppure l'orale

esameScritto = False
esameOrale = True
print("PROFESSORE BRAVO")
if esameScritto or esameOrale:
    print("Complimenti hai superato l'esame")
else:
    print("Mi spiace, non hai superato l'esame+")


print("PROFESSORE CATTIVO")
if esameScritto and esameOrale:
    print("Complimenti hai superato l'esame")
else:
    print("Mi spiace non hai superato l'esame perchè uno dei due è andato male")