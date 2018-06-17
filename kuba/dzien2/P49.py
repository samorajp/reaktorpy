#user: user123
#admin: admin123

konta={
    'user': 'user123',
    'admin': 'admin123'
}

login = input("Podaj login: ")
hasło = input("Podaj hasło: ")
#
# if login in konta:
#     print ("Jest takie konto")
# else:
#     print ("Nieprawidłowy login")
#     exit()
#
# if hasło == konta[login]:
#     print("Zalogowałeś się !")
# else:
#     print("Błędne hasło")

if login in konta and hasło == konta[login]:
    print("Zalogowałeś się!")
    if login == 'admin':
        print("Witaj Mistrzu kodu ! ")
    else:
        print("Witaj Użyszkodniku ! ")
else:
    print("Nieprawidłowy login lub hasło")
