import random
from .player_actions import *

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
                att_roll(self.monster, self.player)
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
                    att_roll(self.monster, self.player)


    def player_turn(self):
        print("a) Attack, b) Flee")
        inp = input("What do you want to do ?").lower()
        if inp == "a":
            att_roll(self.player, self.monster)
        if inp == "b":
            if flee(self.player, self.monster):
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
            self.player.gold += gold
            print(f'You loot {gold} gold pieces for a total of {self.player.gold} gold pieces')
            self.player.xp += self.monster.xp
            self.player.level_up_check()
