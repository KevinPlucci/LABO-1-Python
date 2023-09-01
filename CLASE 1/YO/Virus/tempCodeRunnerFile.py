import random

def get_user_choice():
    while True:
        user_input = input("Elige entre 'Vaccine', 'Virus' o 'Data': ").lower()
        if user_input in ['vaccine', 'virus', 'data']:
            return user_input
        else:
            print("Elección inválida. Por favor, elige una opción válida.")

def get_computer_choice():
    options = ['vaccine', 'virus', 'data']
    return random.choice(options)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate"
    elif (
        (user_choice == 'vaccine' and computer_choice == 'virus') or
        (user_choice == 'virus' and computer_choice == 'data') or
        (user_choice == 'data' and computer_choice == 'vaccine')
    ):
        return "Ganaste"
    else:
        return "Perdiste"

def main():
    play_again = 's'
    while play_again == 's':
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Tú elegiste: {user_choice}")
        print(f"La computadora eligió: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("¿Quieres jugar de nuevo? (s/n): ").lower()

main()