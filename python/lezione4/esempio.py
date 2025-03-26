# Esempio di dichiarazione e uso variabili 
print("Scrivi il tuo nome, caro utente!")

# per poter acquisire qualcosa che digita l'utente utilizzo la funzione input()
# nomeUser = "Jacopo"
nomeUser = input()

print("Benvenuto", nomeUser)

# Faccio la stessa cosa in modo + veloce passando come argomento all'input in una frase
# funzione (argomento) --> FIRMA (questa può essere VUOTA se non è presente nulla all'interno delle parentesi o PIENA se c'è scritto qualcosaa dentro)
cognomeUser = input("Scrivi il tuo cognome.. ")
print("Ik tuo cognome è", cognomeUser)


print("----------NUMERI----------")
# ATTENZIONE: tutto ciò che recupero da un utente è considerato una string, un testo, Per poter fare un calcolo devo fare il TYPE CASTING ovvero forzare quella variabile ad essere un numero e non una stringa

num1 = int(input("Scrivi un numero "))
num2 = int(input("Scrivi un altro numero "))
somma = num1 + num2
print("La somma vale:", somma)
