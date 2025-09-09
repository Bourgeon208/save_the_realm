from .character import Character
from save_the_realm.maps import realm, event

class Monster(Character):
    def __init__(self, name, hp, att, dmg_dice, dmg, init, ac, xp, gold):
        super().__init__(name, hp, att, dmg_dice, dmg, init, ac, xp, gold)
        self.introduction()

    def att_roll(self, target):
        return super().att_roll(target)

    def introduction(self):
        pass

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", 5, 1, (1, 4), 0, 1, 11, 4, (1, 10))

    def introduction(self):
        print("You encounter a Goblin, he's attacking you !")
        print("(ง •̀_•́)ง ")

class Orc(Monster):
    def __init__(self):
        super().__init__("Orc", 12, 3, (1, 6), 2, 0, 12, 12, (5, 25))

    def introduction(self):
        print("You encounter a ferocious Orc, he's attacking you !")
        print("(҂ `з´ )҂ ")

class Ogre(Monster):
    def __init__(self):
        super().__init__("Ogre", 30, 5, (1, 8), 4, -2, 14, 30, (20, 50))

    def introduction(self):
        print("You encounter a huge Ogre, he's attacking you !")
        print("ᕦ(ò_óˇ)ᕤ")

class Dragon(Monster):
    def __init__(self):
        super().__init__("Dragon", 80, 8, (1, 12), 6, 8, 18, 200, (800, 10000))

    def introduction(self):
        print("You encounter a mighty Dragon, he's attacking you !")
        print("ϞϞϞϞ(๑•̀д•́๑)∩")

class Demon(Monster):
    def __init__(self):
        super().__init__("Demon", 180, 13, (3, 18), 6, 0, 22, 500, (8000, 20000))

    def introduction(self):
        print("You encounter a terrible Demon !")
        print("<^-(ಠ益ಠ)")
        print("HOW DARE YOU DISTURB YOUR MASTER ?!")
        inp = input("What do you say ?").lower()
        if "sorry" in inp and "master" in inp:
            self.init = -10
            print("Hmmm I can not tolerate such insolence, I'll let you try to hit me first but anyway...")
        else:
            self.init = 12
        print("YOU SHALL DIE, INSECT !!!")

class RoyalGuard(Monster):
    def __init__(self):
        super().__init__("Royal Guard", 120, 12, (1, 10), 5, 10, 24, 100, (1, 500))

    def introduction(self):
        print("What is that Demon !? Kill him !")
        print("You encounter a Royal Guard, he's attacking you !")
        print("<--(≖ڡ≖)")


class King(Monster):
    def __init__(self):
        super().__init__("The King", 250, 14, (1, 20), 8, 20, 25, 1000, (100000, 1000000))

    def introduction(self):
        print(f"I shall put an end you misery my poor boy...")
        print("You face the King, he's attacking you ! ")
        print("♔♔♔ ( ͡° ͜ʖ ͡°) ♔♔♔")

def after_dragon(result, game_state):
    if result:
        print("Impressive, you've done it, the Dragon is dead !")
        print("Well done, you're now the Hero of the realm \o/")
        print(".....")
        print("Oh wait, you hear a door opening...")
        game_state["map"].insert(-1, ["▐","█","█","█","█","█","█","█","█","█","█","█","█","E","▌"])

def after_demon(result, game_state):
    if result:
        print("IT'S IMPOSSIBLE !!!")
        print("I shall haunt your mind and take control of your body HAHAHAHAHAHA !")
        print(".....")
        print("You feel an horrible pain, you feel your body changing as you slowly become a monster...")
        print("Weeks later, you leave the labyrinth and roam the kingdom you swore to save.")
        game_state["map"] = realm
        game_state["player_line"] = 15
        game_state["player_col"] = 13

monster_map = {
    "G": (Goblin, None),
    "C": (Orc, None),
    "O": (Ogre, None),
    "D": (Dragon, after_dragon),
    "E": (Demon, after_demon),
    "R": (RoyalGuard, None),
    "K": (King, None),
}

