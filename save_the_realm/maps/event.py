def credits(player):
    print("-----------------------")
    print("---- CHARACTER'S STATS ----")
    for var, value in vars(player).items():
        print(f"{var} = {value}")
    print("---------------------------")
    print("The King is dead, you are now the ruler of this doomed kingdom.")
    print("-----------------------")
    print("Thank you for playing !!!")
    print("          --           ")
    print("     -------------     ")
    print("-----------------------")
    print("Credits :")
    print("Developer : Gaëtan")
    print("Playtester : Camil the foolish")
    print("-----------------------")
    print("     -------------     ")
    print("          --           ")

def death():
    print('------------')
    print('| YOU DIED |')
    print('------------')

def human():
    print("You encounter a group of pity humans, they flee in terror as they see you.")
    print("You have no mercy for them and squash them as vermin...")