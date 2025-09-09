def unicorn(player):
    print("You encounter magnificent Unicron, she poses you a riddle.")
    print("⊂◉‿◉つ>")
    print("I am greater than god,")
    print("Eviler than the devil,")
    print("Rich lack of me,")
    print("Poor got plenty of me,")
    print("And if you eat too much of me, you die,")
    inp = input("Who am I ?").lower()

    if inp == "nothing":
        print("Good answer dear knight, I bless you !")
        player.gain_xp(100)
    else:
        print("Wrong answer, good luck in your journey !")