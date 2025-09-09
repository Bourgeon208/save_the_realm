import random
from .character import Character

def dice_roll(modifier = 0, dice = (1, 20)):
    return random.randint(dice[0], dice[1]) + modifier

class Player(Character):
    def __init__(self, name, hp, att, dmg_dice, dmg, init, ac, xp, gold):
        super().__init__(name, hp, att, dmg_dice, dmg, init, ac, xp, gold)
        self.max_hp = hp
        self.hp = hp
        self.level = 1
        self.armor = "Leather"
        self.weapon = "Spear"
        self.supplies = 1
        self.potion = 0
        # self.inventory = {"Supplies" : 1, "Weapon" : "Spear", "Armor" : "Leather", "Potions" : 0}

    def att_roll(self, target):
        return super().att_roll(target)

    def gain_xp(self, xp):
        print(f'You earn {xp} experience')
        self.xp += xp
        self.level_up_check()

    def loot_gold(self, gold):
        gold = dice_roll(dice=gold)
        self.gold += gold
        print(f'You loot {gold} gold pieces for a total of {self.gold} gold pieces')

    def flee(self, tracker):
        if dice_roll(self.init) > dice_roll(tracker.init):
            return True
        else:
            return False

    def level_up_check(self):
        print(f'You currently have {self.xp} experience points.')
        print(f'You need {self.level * 10} experience points to reach level {self.level +1}.')
        if self.xp >= self.level * 10:
            while self.xp >= self.level * 10:
                print('LEVEL UP !')
                self.xp -= self.level * 10
                self.level += 1
                print(f'You are now level {self.level}.')
                print('You can upgrade : a) Strength, b) Dexterity, c) Constitution')
                inp = input('What do you wish to upgrade ?').lower()
                if inp == 'a':
                    self.att += 1
                    self.dmg += 1
                elif inp == 'b':
                    self.init += 1
                    self.ac += 1
                elif inp == 'c':
                    self.max_hp += dice_roll(dice=(1,10))
                self.max_hp += dice_roll(dice=(1,3))
                self.hp = self.max_hp
                if self.level % 2 == 0:
                    self.att += 1
                if self.level % 3 == 0:
                    self.ac += 1
                if self.level % 4 == 0:
                    self.dmg += 1
    #
    # def buy_item(self, item):
    #     if item == "Sword":
    #         if self.sword == True:
    #             print("You already have a sword.")
    #         elif self.gold < 50:
    #             print("You don't have enough gold.")
    #         else:
    #             print("You bought a sword.")
    #             self.dmg_dice = (1,10)
    #             self.gold -= 50
    #             self.sword = True
    #
    #     if item == "Armor":
    #         if self.armor == True:
    #             print("You already have an armor.")
    #         elif self.gold < 80:
    #             print("You don't have enough gold.")
    #         else:
    #             print("You bought an armor.")
    #             self.ac += 2
    #             self.gold -= 80
    #             self.armor = True
    #
    #     if item == "Potion":
    #         if self.gold < 50:
    #             print("You don't have enough gold.")
    #         else:
    #             print("You bought and drink a potion.")
    #             self.hp = self.max_hp
    #             self.gold -= 50
    #
    #     if item == "Elixir of life":
    #         if self.gold < 400:
    #             print("You don't have enough gold.")
    #         else:
    #             print("You bought and drink a potion.")
    #             self.max_hp = self.max_hp + dice_roll(dice=(2,12))
    #             self.hp = self.max_hp
    #             self.gold -= 400
