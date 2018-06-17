# user: user123
# admin: admin123

konta = {
    'user': 'user123',
    'admin': 'admin123'
}

login = input("Podaj login: ")
haslo = input("Podaj haslo: ")

if login in konta and haslo == konta[login]:
    print("Zalogowałeś się!")
    if login == 'admin':
        print("Witaj szanowny władco systemu!")
    else:
        print("Witaj użyszkodniku!")
else:
    print("Nieprawidłowy login lub hasło")

