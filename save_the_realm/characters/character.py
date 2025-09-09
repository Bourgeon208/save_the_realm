from abc import ABC, abstractmethod
import random

def dice_roll(modifier=0, dice=(1, 20)):
    return random.randint(dice[0], dice[1]) + modifier

class Character(ABC):
    def __init__(self, name, hp, att, dmg_dice, dmg, init, ac, xp, gold):
        self.name = name
        self.hp = hp
        self.att = att
        self.dmg = dmg
        self.dmg_dice = dmg_dice
        self.init = init
        self.ac = ac
        self.xp = xp
        self.gold = gold

    @abstractmethod
    def att_roll(self, target):
        att_roll = dice_roll(self.att)
        print(f'{self.name} attacks {target.name} with {att_roll} attack.')
        if att_roll > target.ac:
            dmg_roll = dice_roll(self.dmg, self.dmg_dice)
            target.hp -= dmg_roll
            print(f'{self.name} struck {target.name} for {dmg_roll} damage !')
            print(f'{target.name} got {target.hp} left.')
        else:
            print(f'{self.name} missed {target.name} !')
