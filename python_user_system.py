usuarios = {'admin': '1234'}  # banco de dados inicial

openfirst = input('Log in ou Start: ')

if openfirst == 'Log in':
    print("\n=== Login ===")
    user_input = input('Usuário: ')
    senha_input = input('Senha: ')
    
    if user_input in usuarios and usuarios[user_input] == senha_input:
        print(f'Bem-vindo, {user_input}!')
    else:
        print('Usuário ou senha incorretos.')

elif openfirst == 'Start':
    print('\n=== Bem vindo ao sistema! ===\n')  
    print('Por favor, crie um usuário para continuar.')

    while True:  # fica repetindo até criar corretamente
        novo_usuario = input('Usuário: ')

        if novo_usuario in usuarios:
            print('Usuário já existe. Por favor, escolha outro nome.')
        else:
            nova_senha = input('Senha: ')
            usuarios[novo_usuario] = nova_senha
            print(f'Usuário {novo_usuario} criado com sucesso!')
            break  # sai do while depois de cadastrar

else:
    print('Opção inválida. Por favor, escolha "Log in" ou "Start".')
