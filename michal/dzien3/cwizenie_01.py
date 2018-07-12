tekst = "aadddssklleeoopppsp"

def fun(text):
    dictionary = {}
    for letter in text:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    return dictionary

print(fun(tekst))