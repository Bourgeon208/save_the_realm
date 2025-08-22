import os
import time
import random

from characters import player, monster
from maps import labyrinth, realm

clear = lambda:os.system("clear")
laby = labyrinth.labyrinth
print("Hello adventurer, the king asked of you to kill a Dragon resting in the labyrinth full of monster.")
name = input("What is your name ?")
global player_1
player_1 = player.Player(name, 10, 2, (1,6), 2, 2, 12, 0, 0)
print("Controls are ZQSD to move, C to see character's stats.")

class Encounter:
    def __init__(self, monster):
        self.monster = monster
        self.player = player_1
        self.combat_fled = False

    def combat(self):
        monster_init = self.monster.init + random.randint(1, 20)
        player_init = player_1.init + random.randint(1, 20)
        print(f'{self.monster.name} rolled {monster_init} initiative')
        print(f'{player_1.name} rolled {player_init} initiative')

        while True:
            if self.combat_fled:
                return False
            if self.monster.hp < 1:
                self.end_combat()
                return True
            elif player_1.hp < 1:
                self.end_combat(death=True)
                return False

            if monster_init > player_init:
                att_roll(self.monster, player_1)
                if player_1.hp < 1:
                    self.end_combat(death=True)
                    return False
                else:
                    self.player_turn()
            else:
                self.player_turn()
                if self.monster.hp < 1:
                    self.end_combat()
                    return True
                elif self.combat_fled:
                    return False
                else:
                    att_roll(self.monster, player_1)


    def player_turn(self):
        print("a) Attack, b) Flee")
        inp = input("What do you want to do ?").lower()
        if inp == "a":
            att_roll(player_1, self.monster)
        if inp == "b":
            if flee(player_1, self.monster):
                self.end_combat(flee = True)
            else:
                print('You failed to escape the encounter.')


    def end_combat(self, flee = False, death = False):
        if flee:
            print('You successfully manage to escape the encounter...')
            self.combat_fled = True
        elif death:
            print('You died.')
        else:
            print('You won !')
            print(f'You earn {self.monster.xp} experience')
            gold = dice_roll(dice = self.monster.gold)
            player_1.gold += gold
            print(f'You loot {gold} gold pieces for a total of {player_1.gold} gold pieces')
            player_1.xp += self.monster.xp
            player_1.level_up_check()



def flee(coward, tracker):
    if dice_roll(coward.init) > dice_roll(tracker.init):
        return True
    else:
        return False

def dice_roll(modifier = 0, dice = (1, 20)):
    return random.randint(dice[0], dice[1]) + modifier

def att_roll(attacker, target):
    att_roll = dice_roll(attacker.att)
    print(f'{attacker.name} attacks {target.name} with {att_roll} attack.')
    if att_roll > target.ac:
        dmg_roll = dice_roll(attacker.dmg, attacker.dmg_dice)
        target.hp -= dmg_roll
        print(f'{attacker.name} struck {target.name} for {dmg_roll} damage !')
        print(f'{target.name} got {target.hp} left.')
    else:
        print(f'{attacker.name} missed {target.name} !')


while player_1.hp > 0:
    player_line = player_col = new_player_line = new_player_col = None
    for l in laby:
        if "X" in l:
            player_line = laby.index(l)
            player_col= l.index("X")
        print("".join(l))

    inp = input("Where to go ?").lower()

    while inp not in ["z", "q", "s", "d", "c"]:
        print("Wrong input.")
        inp = input("Where to go ?").lower()

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
        for var, value in vars(player_1).items():
            print(f"{var} = {value}")
        print("---------------------------")

    new_pos = laby[new_player_line][new_player_col]

    if new_pos in ["-", "|", "#"]:
        print("You can't go that way !")
        time.sleep(1)
    elif new_pos == " ":
        laby[player_line][player_col] = " "
        laby[new_player_line][new_player_col] = "X"
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
        laby[player_line][player_col] = " "
        laby[new_player_line][new_player_col] = "X"

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
            encounter = Encounter(monster)
            encounter_result = encounter.combat()
        elif new_pos == "C":
            print("You encounter a ferocious Orc, he's attacking you !")
            print("(҂ `з´ )҂ ")
            monster = monster.Monster("Orc", 12, 3, (1,6), 2, 0, 12, 12, (5,25))
            encounter = Encounter(monster)
            encounter_result = encounter.combat()
        elif new_pos == "O":
            print("You encounter a huge Ogre, he's attacking you !")
            print("ᕦ(ò_óˇ)ᕤ")
            monster = monster.Monster("Ogre", 30, 5, (1,8), 4, -2, 14, 30, (20,50))
            encounter = Encounter(monster)
            encounter_result = encounter.combat()
        elif new_pos == "D":
            print("You encounter a mighty Dragon, he's attacking you !")
            print("ϞϞϞϞ(๑•̀д•́๑)∩")
            monster = monster.Monster("Dragon", 80, 8, (1,12), 6, 8, 18, 200, (800,10000))
            encounter = Encounter(monster)
            encounter_result = encounter.combat()
            if encounter_result:
                print("Impressive, you've done it, the Dragon is dead !")
                print("Well done, you're now the Hero of the realm \o/")
                print(".....")
                print("Oh wait, you hear a door opening...")
                laby.insert(-1, ["|","#","#","#","#","#","#","#","#","#","#","#","#","E","|"])

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
            encounter = Encounter(monster)
            encounter_result = encounter.combat()
            if encounter_result:
                print("IT'S IMPOSSIBLE !!!")
                print("I shall haunt you mind and take control of your body HAHAHAHAHAHA !")
                print(".....")
                print("You feel an horrible pain, you feel your body changing as you slowly become a monster...")
                print("Weeks later, you leave the labyrinth and roam the kingdom you swear to save.")
                laby = realm.realm
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
            encounter = Encounter(monster)
            encounter_result = encounter.combat()

        elif new_pos == "K":
            print(f"{player_1.name}, is that you ?! What happened to you ?!")
            print(f"I shall put an end you misery my poor boy...")
            print("You face the King, he's attacking you ! ")
            print("♔♔♔ ( ͡° ͜ʖ ͡°) ♔♔♔")
            monster = monster.Monster("The King", 250, 14, (1,20), 8, 20, 25, 1000, (100000,1000000))
            encounter = Encounter(monster)
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
            laby[player_line][player_col] = " "
            laby[new_player_line][new_player_col] = "X"



