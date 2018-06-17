#hasło

# admin: admin123
# user: user123

konta = {
    'user': 'user123',
    'admin': 'admin123'
}

login = input('Podaj login:\n')
haslo = input('Podaj hasło:\n')

if login in konta and haslo == konta[login]:
    print('Zalogowałeś się!')

    if login == 'admin':
        print('Witaj szanowny władco systemu!')
    else:
        print('Witaj użyszkodniku!')

else:
    print('Nieprawidłowy login lub hasło')
    exit()




