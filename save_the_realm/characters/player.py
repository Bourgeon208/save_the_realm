class Player:
    def __init__(self, name, max_hp, att, dmg_dice, dmg, init, ac, xp, gold):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.att = att
        self.dmg = dmg
        self.dmg_dice = dmg_dice
        self.init = init
        self.ac = ac
        self.xp = xp
        self.gold = gold
        self.level = 1
        self.armor = False
        self.sword = False

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

    def buy_item(self, item):
        if item == "Sword":
            if self.sword == True:
                print("You already have a sword.")
            elif self.gold < 50:
                print("You don't have enough gold.")
            else:
                print("You bought a sword.")
                self.dmg_dice = (1,10)
                self.gold -= 50
                self.sword = True

        if item == "Armor":
            if self.armor == True:
                print("You already have an armor.")
            elif self.gold < 80:
                print("You don't have enough gold.")
            else:
                print("You bought an armor.")
                self.ac += 2
                self.gold -= 80
                self.armor = True

        if item == "Potion":
            if self.gold < 50:
                print("You don't have enough gold.")
            else:
                print("You bought and drink a potion.")
                self.hp = self.max_hp
                self.gold -= 50

        if item == "Elixir of life":
            if self.gold < 400:
                print("You don't have enough gold.")
            else:
                print("You bought and drink a potion.")
                self.max_hp = self.max_hp + dice_roll(dice=(2,12))
                self.hp = self.max_hp
                self.gold -= 400
