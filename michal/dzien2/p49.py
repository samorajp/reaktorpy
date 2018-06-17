konta = {'admin': 'admin',
          'user': 'user'
}
print('logowanie')
login = input('podaj login\n')
passw = input('podaj hasło\n')

if login == 'admin' and passw == konta[login]:
    print('witaj adminie')
elif login == 'user' and passw == konta[login]:
    print('witaj użytkowniku')
else:
    print('błędne hasło')
#if login in konta: