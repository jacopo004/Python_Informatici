nomeUtente = "Jacopo Pisano"

# in questo caso utilizzo il simbolo + per concatenare delle stringhe
presentazione = "Ciao, " + nomeUtente +  " questa è la Calcolatrice più semplice"
print(presentazione)


numero1 = 42.3
numero2 = 6.4

# Calcolare le 4 operazioni matematiche di base
somma = numero1 + numero2
print("La somma vale: ", somma)

prod = numero1 * numero2
print("Il prodotto vale: ", prod)

sottr = numero1 - numero2
print("La sottrazione vale: ", sottr)

div = numero1 / numero2
print("La divisione vale: ", div)

# elevamento a potenza
# eleviamo alla potenza 2 entrabi i numeri
potenza1 = numero1 ** 2
potenza2 = numero2 ** 2

print("La potenza del primo numero vale:", potenza1)
print("La potenza del secondo numero vale:", potenza2)

#Calcolo la radice quadrata utilizzando le potebze
radice1 = numero1 ** (1/2)
radice2 = numero2 ** (1/2)

print("La radice del primo numero vale:", radice1)
print("La radice del primo numero vale:", radice2)

numeroProva = 2
elevazioneNeg = numeroProva ** (-2) # (1/2)^ 2
print(elevazioneNeg)

numeroProva2 = -2
elevazionePos = numeroProva2 ** 2
print(elevazionePos)


# METODO 2
numero3 = 4
# elevo questo numero alla potenza 2 (pow serve per elevare a potenza)
potenza3 = pow(numero3, 2)
print("La potenza di numero3 alla seconda vale", potenza3)

#calcolo la radice di 4 utilizzando la funzione sqrt
# devo importare la libreria math, sono delle librerie di utilità matematica
# ATTENZIONE, di solito quando si importano le librerie devo importarle in alto nella pagina
import math
radice3 = math.sqrt(numero3)
print("La radice di", numero3, "vale:", radice3)

