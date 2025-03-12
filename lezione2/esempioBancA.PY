# implementare l'operazione di deposito contanti
print("Inserisci il tuo nome")
nome = input()
print("Il mio nome è", nome)


print("Quanto desideri depositare ?")
deposito = int(input())

saldo = 1000

if deposito > 600:
    print("Non puoi")
else:
    saldo += deposito
    print("Il nuovo saldo è", saldo) 
