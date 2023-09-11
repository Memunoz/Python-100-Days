import os
import random
import art
import data


def clear():
    os.system('clear')


def choice():
    while True:
        try:
            choice = str(
                input("\nSeleccione la opcion 'A' o 'B': ").upper())
            if choice == "A" or choice == "B":
                return choice
            else:
                print(
                    "Por favor, seleccione entre la opcion 'A' o 'B': ")
        except ValueError:
            print(
                "Por favor, seleccione entre la opcion 'A' o 'B': ")


def final_choice():
    while True:
        try:
            fin = str(
                input("Quiere jugar nuevamente? (S/N) ").upper())
            if fin == "S":
                clear()
                play()
            elif fin == "N":
                print("Adios!")
                exit()
            else:
                print(
                    "Por favor, seleccione entre S/N ")
        except ValueError:
            print(
                "Por favor, seleccione entre S/N ")


def get_random_account():
    """Get data from random account"""
    return random.choice(data.lista_famosos)


def format_data(account):
    """Format account into printable format: name, description and country"""
    artista = account["famoso"]
    description = account["descripcion"]
    return f"{artista},{description}"


def game():
    global score
    famoso1 = get_random_account()
    famoso2 = get_random_account()

    while famoso1 == famoso2:
        famoso2 = get_random_account()

    print(
        f"Opcion 'A': {format_data(famoso1)}\nVS\nOpcion 'B': {format_data(famoso2)}")

    eleccion = choice()
    A = int(famoso1["seguidores"])
    B = int(famoso2["seguidores"])
    contrario = ()

    if eleccion == "A":
        contrario = B
        eleccion = A
    else:
        contrario = A
        eleccion = B

    if eleccion > contrario:
        score += 1
        clear()
        print(art.logo)
        print(f"\nCorrecto\n{famoso1['famoso']} tiene {famoso1['seguidores']} seguidores y {famoso2['famoso']} tiene {famoso2['seguidores']} seguidres \nPuntaje actual {score}\nVamos por el siguiente!\n")
        game()
    else:
        clear()
        print(art.logo)
        print(
            f"\nIncorrecto!\n{famoso1['famoso']} tiene {famoso1['seguidores']} seguidores y {famoso2['famoso']} tiene {famoso2['seguidores']} seguidres\nPierdes y debes comenzar nuevamente")
        print(f"Tu puntaje final es de {score}")
        final_choice()


score = 0


def play():
    global score
    score = 0
    print(art.logo)
    print("Bienvenido a higerlower.\nEl objetivo es indicar cuales de estas personalidades tiene mas seguidores en IG.\n")
    game()


play()
