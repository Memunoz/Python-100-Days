import os
import random


def clear():
    os.system('clear')


logo = ''' 
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\.
                       _/ |                
                      |__/                 '''

reglas = '''
Reglas:

El objetivo es vencer al crupier (el repartidor) obteniendo una mano cuyo valor sea más cercano a 21 que el valor de la mano del crupier, pero sin exceder 21.
Si la mano del jugador excede 21, pierde automáticamente, sin importar la mano del crupier.
Si el jugador se planta, el crupier juega su mano siguiendo reglas predefinidas.
Si la mano del crupier supera 21, todos los jugadores que no se hayan pasado ganan.
Si la mano del crupier es mejor que la del jugador, el crupier gana.
Si la mano del jugador es mejor y no excede 21, el jugador gana y recibe un pago igual a su apuesta.
En caso de empate, el jugador recupera su apuesta original sin ganar ni perder.\n'''
fichas = 1000


def obtener_apuesta(text):
    while True:
        try:
            apuesta = int(input(text))
            if apuesta <= 0:
                print("La apuesta debe ser mayor que cero.")
            else:
                return apuesta
        except ValueError:
            print("Por favor, ingresa un número válido.")


def obtener_respuesta(mensaje):
    while True:
        respuesta = input(mensaje).lower()
        if respuesta == "si" or respuesta == "no":
            return respuesta
        else:
            print("Por favor, responde con 'si' o 'no'.")


cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def actualizar_cartas(player_card):
    if "A" in player_card:
        print("Tienes una carta 'A' en tu mano.")
        while True:
            opcion = input("¿Quieres cambiar el valor de 'A' a 1 o a 11? ")
            if opcion == "1" or opcion == "11":
                opcion = int(opcion)
                break
            else:
                print("Opción inválida. Por favor, elige '1' o '11'.")

        player_card = [1 if carta == "A" and opcion == 1 else (
            11 if carta == "A" and opcion == 11 else carta) for carta in player_card]

    return player_card


def convertir_a_enteros(lista):
    try:
        lista_enteros = [int(valor) for valor in lista]
        return lista_enteros
    except ValueError:
        print("Error: Alguno de los valores no es convertible a entero.")


def check_and_replace(hand):
    if "A" in hand:
        index_of_A = hand.index("A")
        hand_with_11 = hand.copy()
        hand_with_11[index_of_A] = 11
        hand_with_11 = convertir_a_enteros(hand_with_11)

        if sum(hand_with_11) > 21:
            hand[index_of_A] = 1
        else:
            hand[index_of_A] = 11

    return hand


def calculate_score(cards):
    check_and_replace(cards)
    total_score = sum(cards)
    if total_score == 21:
        total_score = 0

    return total_score


def compare(jugador, manoa, pc, manob, bet):
    global fichas
    print(
        f"\nCartas del jugador: {manoa} = {jugador}\nCartas del Crupier: {manob} = {pc}")
    if pc == 0:
        fichas -= bet
        print("El oponente tiene Blackjack, Pierdes! 😱\n")
        return
    elif jugador == pc:
        print("Empate 🙃\n")
        return
    elif jugador == 0:
        fichas += bet
        print("Ganas! con Blackjack 😎\n")
        return
    elif jugador > 21:
        fichas -= bet
        print("Te pasaste, Pierdes! 😭\n")
        return
    elif pc > 21:
        fichas += bet
        print("El Crupier se paso, Ganas! 😁\n")
        return
    elif jugador > pc:
        fichas += bet
        print("Ganas! 😃\n")
        return
    else:
        fichas += bet
        print("Pierdes! 😤\n")
        return


def black_jack():
    global fichas
    player_card = []
    pc_card = []
    player_card.append(deal_card())
    player_card.append(deal_card())
    pc_card.append(deal_card())
    pc_card.append(deal_card())

    should_continue = True
    print(f"Te quedan {fichas} fichas")
    apuesta = obtener_apuesta("Cuánto deseas apostar? ")

    while apuesta > fichas:
        print(
            "La apuesta es mayor que la cantidad de fichas disponibles. Intente nuevamente.")
        apuesta = obtener_apuesta("Cuánto deseas apostar? ")

    print(f"El crupier saco un {pc_card[0]}")
    print(f"Tus cartas son {player_card} ")

    pc_hand = calculate_score(pc_card)

    actualizar_cartas(player_card)
    player_hand = calculate_score(player_card)
    print(f"Con un total de {player_hand}")

    while should_continue and player_hand <= 21:

        answer = obtener_respuesta("Quieres otra carta? (si/no) ")

        if answer.lower() == "si":
            player_card.append(deal_card())
            actualizar_cartas(player_card)
            player_hand = calculate_score(player_card)
            print(
                f"Obtienes un {player_card[-1]} para un total de {player_hand}")
        else:
            should_continue = False

    while pc_hand < 17:
        pc_card.append(deal_card())
        pc_hand = calculate_score(pc_card)

    compare(player_hand, player_card, pc_hand, pc_card, apuesta)

    if fichas <= 0:
        print(f"Te quedan {fichas} fichas.")
        print("\nPOR FAVOR RECARGA TU CUENTA, No te quedan fichas!")
        answer3 = obtener_respuesta("Quieres jugar de vuelta? (si/no) ")
        if answer3.lower() == "si":
            fichas = 1000
            game()
        else:
            exit()

    print(f"Te quedan {fichas} fichas.")
    answer2 = obtener_respuesta("Quieres jugar de vuelta? (si/no) ")

    if answer2.lower() == "si":
        clear()
        print(logo)
        print(reglas)
        return black_jack()
    else:
        fichas = 1000
        game()


def game():
    clear()
    print(logo)
    print(reglas)
    print("Comienzas con 1000 fichas")
    black_jack()


game()
black_jack()
