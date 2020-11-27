def computer():
    print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach")
    list = ["zgadłeś", "za mało", "za dużo"]
    min = 0
    max = 1000
    guess = int((max-min)/2) + min
    print(f"Zgaduję: {guess}")
    user = ""
    attemps = 1
    while user != list[0]:
        try:
            user = input("Podaj: ")
            if attemps < 10:
                if user == list[2]:
                    max = guess
                    guess = int((max-min)/2) + min
                    print(f"Zgaduję: {guess}")
                    attemps += 1
                elif user == list[1]:
                    min = guess
                    guess = int((max-min)/2) + min
                    print(f"Zgaduję: {guess}")
                    attemps += 1
                else:
                    raise ValueError
            else:
                return print("Nie oszukuj")
        except ValueError:
            print("niedozwolone słowo")
    print("Wygrałem")


computer()
