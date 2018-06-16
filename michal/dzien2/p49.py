loginy = {'admin': 'admin',
          'user': 'user'
}
print('logowania')
user = input('podaj login')
passw = input('podaj hasło')

if user == 'admin' and passw == loginy[user]:
    print('witaj adminie')
elif user == 'user' and passw == loginy[user]:
    print('witaj użytkowniku')
else:
    print('błędne hasło')