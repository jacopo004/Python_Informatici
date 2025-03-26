# Instanziare una variabie "saldo" = 1000

# Chiedere all'utente quanto ha guadagnato questo mese (utilizza un valore con la virgola)
# se l'utente ha guadagnato ppiù di 1000 euro stampare: "Bravo, quesato mese hai guadagnato bene". Calcolare il saldo su 10000 euro (guadagno 1500, incasso (10000 + 1500) = 10500)

# se l'utente ha guadagnato meno di 1000 euro stampare: ("Mi spiace, questo mese hai guadagnato così così"). Calcolare il saldo su 1000 euro

# se l'utente ha guadagnato 0 stampare: "Questo mese non hai guadagnato nulla". Calcolare il saldo 

# se l'utente è andato in perdita stampare: "Questo mese stai perdendo soldi". Calcolare il saldo

saldo = 10000
guadagno = float(input("Quantu ha guadagnato in questo mese? ")) #questa operazione è definita typecasting


if guadagno < 0:
    print("Questo mese stai perdendo soldi")
    saldo = saldo + guadagno
elif guadagno == 0:
    print("Questo mese non hai guadagnato nulla")
    saldo = saldo + guadagno
elif guadagno < 1000:
    print("Mi spiace, questo mese hai guadagnato così così")
    saldo = saldo + guadagno 
else:
    print("Bravo, questo mese hai guadagnato bene")
    saldo = saldo + guadagno 

print("Il tuo saldo è di: ", saldo)