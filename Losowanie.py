import sys
print("gra w zgadnij imie ")
print("wybierz poziom trudnosci: (1, 2 lub 3)")
print("1 - latwy - 15 prob")
print("2 - sredni - 10 prob")
print("3 - trudny - 5 prob")
a = int(input())
if a == 1: b=15
if a == 2: b=10
if a == 3: b=5
ilosc_prob = b
slowo = "kamila"
used_letter = []
user_word = []

def find_indexes(slowo, litera):
    indexes = []
    for index, letter_in_word in enumerate(slowo):
        if litera == letter_in_word:
            indexes.append(index)
    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print("Pozostalo prob: ", ilosc_prob)
    print("Uzyte litery: ", used_letter)
    print()


# mozna uzyc zamiast letter  ==  _
for letter in slowo:
    user_word.append("*")

while True:
    litera = input("podaj litere: ")
    found_letter = find_indexes("".join(used_letter), litera)
    if len(found_letter) != 0:
        print("taka litera juz byla ")
    else:
        used_letter.append(litera)

    found_indexes = find_indexes(slowo, litera)
    if len(found_indexes) == 0:
        print("Nie ma takiej litery")
        ilosc_prob -= 1

        if ilosc_prob == 0:
            print("Koniec gry ")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = litera

            if "".join(user_word) == slowo:
                print("Brawo, to jest to haslo")
                sys.exit(9)

    show_state_of_game()

