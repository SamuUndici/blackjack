import random

carte = [1 ,2, 3 , 4, 5, 6, 7 , 8, 9,10]
carte_usate = []
banco = []
#scelgo le due carte del banco 
#IL BANCO STA A 17 
carta1b   = random.choice(carte)
carta2b  = random.choice(carte)
#scelgo le due carte del giocatore
carta1g = random.choice(carte)
carta2g = random.choice(carte)
print("il banco ha questa carta: ", carta1b)
print("La tua mano è: ", carta1g , carta2g, ", il risultato è: ", carta1g+carta2g)

gioco = input(print("cosa vuoi fare? Carta (Y) o stai (N)?"))
if gioco == "Y" or gioco == "y":    
    print("continuo")
else: print("non continuo")
 

#controllo la somma delle carte del giocatore
#controllo possibili combinazioni (asso + figura = bj , 2+ figura = 2 o 12 ecc)
#restituisco il messaggio contenente il risultato e chiedo al giocatore se vuole un'altra carta o se sta
#in base alla scelta del giocatore controllo il risultato e 1) do carta e restituisco il risultato 2) controllo il banco e agisco di conseguenza


