def computer():
    print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach")
    min = 0
    max = 1000
    guess = int((max-min)/2) + min
    print(f"Zgaduję: {guess}")
    user = ""
    attemps = 1
    while user != "zgadłeś":
        user = input("Podaj: ")
        if attemps < 10:
            if user == "za dużo":
                max = guess
                guess = int((max-min)/2) + min
                print(f"Zgaduję: {guess}")
                attemps += 1
            else:
                min = guess
                guess = int((max-min)/2) + min
                print(f"Zgaduję: {guess}")
                attemps += 1
        else:
            return print("Nie oszukuj")
    print("Wygrałem")


computer()
