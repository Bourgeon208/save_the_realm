import random
import os

clear = lambda:os.system("clear")

class Encounter:
    def __init__(self, monster, player):
        self.monster = monster
        self.player = player
        self.combat_fled = False

    def combat(self):
        monster_init = self.monster.init + random.randint(1, 20)
        player_init = self.player.init + random.randint(1, 20)
        print(f'{self.monster.name} rolled {monster_init} initiative')
        print(f'{self.player.name} rolled {player_init} initiative')

        while True:
            if self.combat_fled:
                return False
            if self.monster.hp < 1:
                self.end_combat()
                return True
            elif self.player.hp < 1:
                self.end_combat(death=True)
                return False

            if monster_init > player_init:
                self.monster.att_roll(self.player)
                if self.player.hp < 1:
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
                    self.monster.att_roll(self.player)
            clear()

    def player_turn(self):
        options = {"a", "b"}
        while (inp := input("a) Attack, b) Flee\nWhat do you want to do ? ").lower()) not in options:
            print("Wrong input.")

        if inp == "a":
            self.player.att_roll(self.monster)
        if inp == "b":
            if self.player.flee(self.monster):
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
            self.player.loot_gold(self.monster.gold)
            self.player.gain_xp(self.monster.xp)
