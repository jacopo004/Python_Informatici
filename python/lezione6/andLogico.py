# L' AND logico oppure (&&) ,o permette di unire più condizioni. Vuol dire che ho bisogno che entrambe le condizioni siano valide affinchè tutta la condizione sia true.

#Giangiacomo compie 18 anni, da oggi può accedre al club dei programmatori ma deve avere un invito

etaGiangiacomo = 17
invito = False # invito è già un boolean. Non ho necessità di valutarlo

if etaGiangiacomo >= 18 and invito:
    print("Ciao Giangi, puoi far parte del club dei programmatori")
elif etaGiangiacomo < 18 and invito:
    print("Caro Giangi, non hai ancora compiuto 18 anni. Anche se hai l'invito non puoi entrare")
elif etaGiangiacomo >= 18 and not invito: # il NOT logico nega una condizione
    print("Caro Giangi, pur avendo 18 anni non puoi entrare poichè ti manca l'invito")
else:
    print("Mi spiace, non puoi far parte del club. Non hai 18 anni e non hai neppure un invito")


# continua il codice chiedendo all'utente il suo nome, l'età e se possiede l'invuto

nome = input("Qual è il tuo nome? ")
eta = int(input("Quanti anni hai? "))
invito = input("Hai l'invito? ")

if eta >= 18 and invito == "Si":
    print("Benvenuto nel club")
elif eta < 18 and invito == "Si":
    print("Mi spiace, non avendo l'età adeguata non ti è consentito entrare")
elif eta >= 18 and invito == "No":
    print("Mi spiace, anhce se hai l'età giusta, non avendo l'invito non ti è consentito entrare")
else:
    print("Mi spiace, ma non avendo nessuna delle due condizioni non ti è possibile partecipare")
