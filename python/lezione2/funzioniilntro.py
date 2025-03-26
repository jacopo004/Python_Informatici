# funzioni built-in: sono funzioni che appartengono al linguaggio stesso
print("Anche print è una funzione built-in")

print("Inserisci il tuo nome")
nome = input() # input()è una funzione built che mi permette di ricevere in input un valore e registrarlo in una variabile
print("Ciao", nome)

saldo = 1000

print("Quanto desideri prelevare ?")
prelievo = int(input()) # sto forzando l'input ad essere un intero: CAST del dato

if prelievo > 500:
    print("Mi spiace, non puoi prelevare più di 500")
else:
    if prelievo > saldo:
        print("Mi spice non hai abbastanza soldi")
    else:
        saldo -= prelievo
        print("Il tuo saldo attuale è", saldo)

