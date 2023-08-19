import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

choice = int(input("Elije 1 para piedra, 2 para papel o 3 para tijera\n"))
random_choice = random.randint(1, 3)
jugador = ""
oponente = ""
if choice == 1:
    jugador = rock
elif choice == 2:
    jugador = paper
elif choice == 3:
    jugador = scissors
else:
    print("Dije 1, 2 o 3... no es muy complicado...")
    exit()
if random_choice == 1:
    oponente = rock
elif random_choice == 2:
    oponente = paper
elif random_choice == 3:
    oponente = scissors

print(f"\nElejiste \n{jugador}\n y tu oponente elijio \n{oponente}\n")

if choice == 1:
    if random_choice == 1:
        print("Empate")
    elif random_choice == 2:
        print('Perdiste')
    else:
        print('Ganaste!')
elif choice == 2:
    if random_choice == 1:
        print('Ganaste!')
    elif random_choice == 2:
        print('Empate')
    else:
        print('Perdiste')
elif choice == 3:
    if random_choice == 1:
        print('Perdiste')
    elif random_choice == 2:
        print('Ganaste!')
    else:
        print('Empate')
else:
    print('No has elegido una opción válida.')
