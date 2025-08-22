import time

from characters import player, monster
from maps import labyrinth, realm, movement
from combats import encounter

map = labyrinth.labyrinth
print("Greetings adventurer, the king asked of you to kill a Dragon resting in the labyrinth full of monster.")
name = input("What is your name ?")
global player_1
player_1 = player.Player(name, 10, 2, (1,6), 2, 2, 12, 0, 0)
print("Controls are ZQSD to move, C to see character's stats.")

while player_1.hp > 0:
    new_player_line, new_player_col, player_line, player_col = movement.movement(map, player_1)
    new_pos = map[new_player_line][new_player_col]

    if new_pos in ["-", "|", "#"]:
        print("You can't go that way !")
        time.sleep(1)
    elif new_pos == " ":
        map[player_line][player_col] = " "
        map[new_player_line][new_player_col] = "X"
    elif new_pos == "U":
        print("You encounter magnificent Unicron, she poses you a riddle.")
        print("⊂◉‿◉つ>")
        print("I am greater than god,")
        print("Eviler than the devil,")
        print("Rich lack of me,")
        print("Poor got plenty of me,")
        print("And if you eat to much of me, you die,")
        inp = input("Who am I ?").lower()

        if inp == "nothing":
            print("Good answer dear knight, I bless you !")
            print(f"{player_1.name} been awarded 100 experience points")
            player_1.xp += 100
            player_1.level_up_check()
        else:
            print("Wrong answer, good luck in your journey !")
        map[player_line][player_col] = " "
        map[new_player_line][new_player_col] = "X"

    elif new_pos == "S":
        print("You encounter a friendly Merchant, he proposes to trade.")
        print("(͡• ͜ʖ ͡•)")
        print("a) Sword (50 gold), b) Armor (80 gold), c) Potion (50 gold), d) Elixir of life (400 gold), e) Leave the shop")
        while True:
            inp = input("What to do ?").lower()
            if inp == "a":
                player_1.buy_item("Sword")
            if inp == "b":
                player_1.buy_item("Armor")
            if inp == "c":
                player_1.buy_item("Potion")
            if inp == "d":
                player_1.buy_item("Elixir of life")
            if inp == "e":
                break
    else:
        encounter_result = False
        dragon = False

        if new_pos == "G":
            print("You encounter a Goblin, he's attacking you !")
            print("(ง •̀_•́)ง ")
            monster = monster.Monster("Goblin", 5, 1, (1,4), 0, 1, 11, 4, (1,10))
            encounter = encounter.Encounter(monster, player_1)
            encounter_result = encounter.combat()
        elif new_pos == "C":
            print("You encounter a ferocious Orc, he's attacking you !")
            print("(҂ `з´ )҂ ")
            monster = monster.Monster("Orc", 12, 3, (1,6), 2, 0, 12, 12, (5,25))
            encounter = encounter.Encounter(monster, player_1)
            encounter_result = encounter.combat()
        elif new_pos == "O":
            print("You encounter a huge Ogre, he's attacking you !")
            print("ᕦ(ò_óˇ)ᕤ")
            monster = monster.Monster("Ogre", 30, 5, (1,8), 4, -2, 14, 30, (20,50))
            encounter = encounter.Encounter(monster, player_1)
            encounter_result = encounter.combat()
        elif new_pos == "D":
            print("You encounter a mighty Dragon, he's attacking you !")
            print("ϞϞϞϞ(๑•̀д•́๑)∩")
            monster = monster.Monster("Dragon", 80, 8, (1,12), 6, 8, 18, 200, (800,10000))
            encounter = encounter.Encounter(monster, player_1)
            encounter_result = encounter.combat()
            if encounter_result:
                print("Impressive, you've done it, the Dragon is dead !")
                print("Well done, you're now the Hero of the realm \o/")
                print(".....")
                print("Oh wait, you hear a door opening...")
                map.insert(-1, ["|","#","#","#","#","#","#","#","#","#","#","#","#","E","|"])

        elif new_pos == "E":
            print("You encounter a terrible Demon !")
            print("<^-(ಠ益ಠ)")
            print("HOW DARE YOU DISTURB YOUR MASTER ?!")
            inp = input("What do you say ?").lower()
            if "sorry" in inp and "master" in inp:
                init = -10
                print("Hmmm I can not tolerate such insolence, I'll let you try to hit me first but anyway...")
            else:
                init = 12
            print("YOU SHALL DIE, INSECT !!!")

            monster = monster.Monster("Demon", 180, 13, (3,18), 6, init, 22, 500, (8000,20000))
            encounter = encounter.Encounter(monster, player_1)
            encounter_result = encounter.combat()
            if encounter_result:
                print("IT'S IMPOSSIBLE !!!")
                print("I shall haunt you mind and take control of your body HAHAHAHAHAHA !")
                print(".....")
                print("You feel an horrible pain, you feel your body changing as you slowly become a monster...")
                print("Weeks later, you leave the labyrinth and roam the kingdom you swear to save.")
                map = realm.realm
                new_player_line = 15
                new_player_col = 13
        elif new_pos == "H":
            print("You encounter a group of pity humans, they flee in terror as they see you.")
            print("You have no mercy for them and squash them as vermin...")
            encounter_result = True

        elif new_pos == "R":
            print("What is that Demon !? Kill him !")
            print("You encounter a Royal Guard, he's attacking you !")
            print("<--(≖ڡ≖)")
            monster = monster.Monster("Royal Guard", 120, 12, (1,10), 5, 10, 24, 100, (1,500))
            encounter = encounter.Encounter(monster, player_1)
            encounter_result = encounter.combat()

        elif new_pos == "K":
            print(f"{player_1.name}, is that you ?! What happened to you ?!")
            print(f"I shall put an end you misery my poor boy...")
            print("You face the King, he's attacking you ! ")
            print("♔♔♔ ( ͡° ͜ʖ ͡°) ♔♔♔")
            monster = monster.Monster("The King", 250, 14, (1,20), 8, 20, 25, 1000, (100000,1000000))
            encounter = encounter.Encounter(monster, player_1)
            encounter_result = encounter.combat()
            if encounter_result:
                print("-----------------------")
                print("---- CHARACTER'S STATS ----")
                for var, value in vars(player_1).items():
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
                break

        if encounter_result:
            map[player_line][player_col] = " "
            map[new_player_line][new_player_col] = "X"

if player_1.hp < 1:
    print('------------')
    print('| YOU DIED |')
    print('------------')

