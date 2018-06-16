#user: user123
#admin: admin123

konta={
    "user": "user123",
    "admin":"admin123"

}
login = input("Podaj login: ")
haslo = input("Podaj hasło: ")

if login in konta and haslo == konta[login]: #czy mamy w sowniku konta, klucz login
    print("Zalogowales się")
else:
    print("NIeprawidłowy login lub haslo")
    exit()

if login =="admin":
    print("Witaj władco systemu")
else:
    print("Witaj użyszkodniku")