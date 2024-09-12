import random
import time

carte = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Scelgo le carte iniziali del giocatore e del banco
carta1g = random.choice(carte)
carte.remove(carta1g)

carta1b = random.choice(carte)
carte.remove(carta1b)

carta2g = random.choice(carte)
carte.remove(carta2g)

print("La tua prima carta è:", carta1g)
time.sleep(2)
print("La prima carta del banco è:", carta1b)
time.sleep(2)
print("La tua seconda carta è:", carta2g)
time.sleep(2)

# Calcolo il risultato del giocatore
risultatog = carta1g + carta2g
print("Il tuo risultato è:", risultatog)

if risultatog > 21:
    print("Hai sballato, il banco vince")
else:
    while True:
        gioco = input("Cosa vuoi fare? Vuoi un'altra carta (Y) o stai? (N) ").lower()
        if gioco == "y":
            nuova_carta = random.choice(carte)
            carte.remove(nuova_carta)
            risultatog += nuova_carta
            print("Hai pescato:", nuova_carta)
            time.sleep(2)
            print("Il tuo nuovo risultato è:", risultatog)
            time.sleep(2)
            if risultatog == 21:
                print("BLACKJACK! Hai vinto!")
                break
            elif risultatog > 21:
                print("Hai sballato, il banco vince")
                break
        elif gioco == "n":
            print("Hai deciso di stare, ora il banco rivela la sua seconda carta. RICORDA: il banco sta a 17")
            carta2b = random.choice(carte)
            carte.remove(carta2b)
            print("La seconda carta del banco è:", carta2b)
            risultatob = carta1b + carta2b
            print("Il banco ha un risultato di", risultatob)
            time.sleep(2)
            if risultatob > risultatog and risultatob <= 21:
                print("Il banco vince.")
                break
            elif risultatob == risultatog:
                print("Parità.")
                break
            while risultatob < 17:
                print("Il banco pesca un'altra carta.")
                time.sleep(2)
                nuova_carta_banco = random.choice(carte)
                carte.remove(nuova_carta_banco)
                risultatob += nuova_carta_banco
                print("Il banco ha pescato", nuova_carta_banco, "e ora ha un totale di", risultatob)
                time.sleep(2)
                if risultatob > 21:
                    print("Il banco ha sballato. Hai vinto!")
                    break
                elif risultatob > risultatog and risultatob <= 21:
                    print("Il banco vince.")
                    break
                elif risultatob == risultatog:
                    print("Parità.")
                    break
            if risultatob >= 17:
                print("Il banco ha fatto", risultatob, ".")
                if risultatob > 21:
                    print("Il banco ha sballato. Hai vinto!")
                elif risultatob == risultatog:
                    print("Parità.")
                else:
                    print("Il banco vince.")
            break
        else:
            print("Inserisci una scelta valida (Y o N)")