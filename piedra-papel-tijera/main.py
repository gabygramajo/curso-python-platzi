user_option = input('User: Elije Piedra, Papél o Tijera: ').lower()
computer_option = input('Computer: Elije Piedra, Papél o Tijera: ').lower()

if user_option == computer_option:
    print('Empate!')
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('Piedra gana a Tijera, has ganado!')
    else:
        print('Papel gana a Piedra, has perdido!')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('Papel gana a Piedra, has ganado!')
    else:
        print('Tijera gana a Papel, has perdido!')
elif user_option == 'tijera':
    if computer_option == 'papel':
        print('Tijera gana a Papel, has ganado!')
    else:
        print('Piedra gana a Tijera, has perdido!')