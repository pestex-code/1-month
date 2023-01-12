import random

def hangman():
    word = random.choice(["kot", "pies", "krowa", "słoń", "małpa"])
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("Zgadłeś! Gratulacje!")
            break

        print("Zgaduj literę:", main)
        guess = input()

        if guess in valid_letters:
            guessmade = guessmade + guess
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 prób pozostało.")
            if turns == 8:
                print("8 prób pozostało.")
                print("       ____________")
            if turns == 7:
                print("7 prób pozostało.")
                print("       ____________")
                print("       |          |")
            if turns == 6:
                print("6 prób pozostało.")
                print("       ____________")
                print("       |          |")
                print("       0          |")
            if turns == 5:
                print("5 prób pozostało.")
                print("       ____________")
                print("       |          |")
                print("       0          |")
                print("      /           |")
            if turns == 4:
                print("4 próby pozostało.")
                print("       ____________")
                print("       |          |")
                print("       0          |")
                print("      / \         |")
            if turns == 3:
                print("3 próby pozostało.")
                print("       ____________")
                print("       |          |")
                print("       0          |")
                print("      / \         |")
                print("       |          |")
            if turns == 2:
                print("2 próby pozostało.")
                print("       ____________")
                print("       |          |")
                print("       0          |")
                print("      / \         |")
                print("       |          |")
                print("      /           |")
            if turns == 1:
                print("1 próba pozostała.")
                print("       ____________")
                print("       |          |")
                print("       0          |")
                print("      / \         |")
                print("       |          |")
                print("      / \         |")
            if turns == 0:
                print
