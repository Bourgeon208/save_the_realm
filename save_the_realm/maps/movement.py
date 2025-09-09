import os

clear = lambda:os.system("clear")

def movement(map, player):
    player_line = player_col = new_player_line = new_player_col = None
    for l in map:
        if "X" in l:
            player_line = map.index(l)
            player_col = l.index("X")
        print("".join(l))

    options = {"z", "q", "s", "d", "c", "r"}
    while (inp := input("Where to go ? ").lower()) not in options:
        print("Wrong input.")

    clear()
    new_player_line = player_line
    new_player_col = player_col
    if inp == "z":
        new_player_line = int(player_line) - 1
        new_player_col = player_col
    elif inp == "q":
        new_player_line = player_line
        new_player_col = player_col - 1
    elif inp == "s":
        new_player_line = int(player_line) + 1
        new_player_col = player_col
    elif inp == "d":
        new_player_line = player_line
        new_player_col = player_col + 1
    elif inp == "c":
        print("---- CHARACTER'S STATS ----")
        for var, value in vars(player).items():
            print(f"{var} = {value}")
        print("---------------------------")
    elif inp == "r":
        print("You rest for the a while.")

    return new_player_line, new_player_col, player_line, player_col