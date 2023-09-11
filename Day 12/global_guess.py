import random


def play_game():
    print("Bienvenido al juego de la adivinanza")

    while True:
        # Genera un número objetivo aleatorio entre 1 y 100
        GOAL = random.randint(1, 100)
        atemps = 0  # Inicializa el contador de intentos
        lower_bound = 1  # Límite inferior para las suposiciones
        upper_bound = 100  # Límite superior para las suposiciones

        # Función para comparar la suposición del usuario con el número objetivo
        def compare(value):
            nonlocal atemps, lower_bound, upper_bound

            if value == GOAL:
                print("¡Ganaste!")
                return True
            elif value < GOAL:
                print('Demasiado bajo')
                # Ajusta el límite inferior
                lower_bound = max(lower_bound, value + 1)
                atemps -= 1
            else:
                print('Demasiado alto')
                # Ajusta el límite superior
                upper_bound = min(upper_bound, value - 1)
                atemps -= 1

            # Verifica si los intentos se agotaron
            if atemps == 0:
                print("¡Se acabaron los intentos! El número correcto era", GOAL)
            else:
                print(
                    f"Intentos restantes: {atemps}. Elegir un número entre {lower_bound} y {upper_bound}")

        # Función para que el usuario ingrese su suposición
        def choice():
            while True:
                try:
                    numero = int(
                        input(f"Ingrese un número entre {lower_bound} y {upper_bound}: "))
                    if lower_bound <= numero <= upper_bound:
                        return numero
                    else:
                        print(
                            f"El número debe estar entre {lower_bound} y {upper_bound}. Intente nuevamente.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

        # Función para que el usuario elija la dificultad
        def dif_choice():
            while True:
                try:
                    choice = str(
                        input("Seleccione entre dificultad 'Facil' o 'Dificil': ").lower())
                    if choice == "facil" or choice == "dificil":
                        return choice
                    else:
                        print(
                            "Por favor, seleccione entre dificultad 'Facil' o 'Dificil': ")
                except ValueError:
                    print(
                        "Por favor, seleccione entre dificultad 'Facil' o 'Dificil': ")

        # Pide al usuario que elija la dificultad
        dificultad = dif_choice()

        # Configura la cantidad de intentos basado en la dificultad elegida
        if dificultad == "facil":
            atemps = 10
        else:
            atemps = 5

        # Bucle principal del juego
        while atemps > 0:
            guess = choice()  # Obtiene la suposición del usuario
            if compare(guess):  # Compara la suposición con el objetivo
                break  # Sale del bucle si el jugador gana

        # Pregunta si el jugador quiere jugar de nuevo
        play_again = input("¿Quieres jugar de nuevo? (s/n): ")
        while play_again.lower() not in ['s', 'n']:
            play_again = input(
                "Por favor, ingresa 's' para sí o 'n' para no: ")

        if play_again.lower() == "n":
            print("¡Gracias por jugar!")
            break  # Termina el juego si el jugador no quiere jugar de nuevo


play_game()  # Inicia el juego
