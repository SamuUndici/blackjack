import random
import time
carte = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
carte_usate = []
banco = []



# Scelgo la prima carta del giocatore
carta1g = random.choice(carte)
carte.remove(carta1g)

# Scelgo la carta del banco
carta1b = random.choice(carte)
carte.remove(carta1b)  # Rimuovi la carta dalla lista delle carte disponibili

#scelgo la seconda carta del giocatore
carta2g = random.choice(carte)
carte.remove(carta2g)

print("Hai questa carta: ", carta1g)
time.sleep(1.5)
print("Il banco ha questa carta: ", carta1b)
time.sleep(1.5)
print("La tua seconda carta è: ", carta2g)
time.sleep(1.5)



# Controllo sul risultato, se è meno di 21 chiedere cosa si vuole fare 
risultatog = carta1g + carta2g
print("Il tuo risultato è: ", risultatog)
if risultatog > 21:
    print("Hai sballato, il banco vince")
else:
    while True:  # Loop per continuare a chiedere finché il giocatore non decide di stare o sballa
        gioco = input("Cosa vuoi fare? Vuoi un'altra carta (Y) o stai? (N) ").lower()
        if gioco == "y":
            nuova_carta = random.choice(carte)  # Pesca una nuova carta
            carte.remove(nuova_carta)
            risultatog += nuova_carta
            print("Hai pescato: ", nuova_carta)
            print("Il tuo nuovo risultato è: ", risultatog)
            
            if risultatog > 21:
                print("Hai sballato, il banco vince")
                break
        elif gioco == "n":
            
            break
        else:
            print("Inserisci una scelta valida (Y o N)")

#controllo la somma delle carte del giocatore
#controllo possibili combinazioni (asso + figura = bj , 2+ figura = 2 o 12 ecc)
#restituisco il messaggio contenente il risultato e chiedo al giocatore se vuole un'altra carta o se sta
#in base alla scelta del giocatore controllo il risultato e 1) do carta e restituisco il risultato 2) controllo il banco e agisco di conseguenza


