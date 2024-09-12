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

print("La tua prima carta è: ", carta1g)
time.sleep(2)
print("La prima carta del banco è: ", carta1b)
time.sleep(2)
print("La tua seconda carta è: ", carta2g)
time.sleep(2)



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
            print("Hai deciso di stare, ora il banco rivela la sua seconda carta. RICORDA: il banco sta a 17")
            carta2b = random.choice(carte)
            carte.remove(carta2b)
            print("La seconda carta del banco è: ", carta2b)
            risultatob = carta1b + carta2b
            print("Il banco ha fatto ",risultatob,".")
            time.sleep(2)
            if risultatob > risultatog:
                print("Il banco vince.")
                break
            elif (risultatob == risultatog):
                print("Parità.")
                break
            while risultatob <= 17:
                print("Il banco pesca un'altra carta.")
                time.sleep(2)
                carte_agg = []
                carte_agg = random.choice(carte)
                carte.remove(carte_agg)
                risultatob = risultatob+carte_agg
                print("Il banco ha pescato ", carte_agg, "il banco ora è a ", risultatob )
                time.sleep(2)
            if risultatob <= 21 or (risultatob == 17 and risultatob>risultatog): 
             print("Il banco ha fatto ", risultatob, "il banco vince. Hai perso.")
             break
            else: print("Il banco ha fatto ", risultatob, ", il banco ha sballato. Hai vinto.")
            time.sleep(2)
            False
        else:
            print("Inserisci una scelta valida (Y o N)")

#controllo la somma delle carte del giocatore
#controllo possibili combinazioni (asso + figura = bj , 2+ figura = 2 o 12 ecc)
#restituisco il messaggio contenente il risultato e chiedo al giocatore se vuole un'altra carta o se sta
#in base alla scelta del giocatore controllo il risultato e 1) do carta e restituisco il risultato 2) controllo il banco e agisco di conseguenza


