import random

def dice_roll(modifier = 0, dice = (1, 20)):
    return random.randint(dice[0], dice[1]) + modifier

def flee(coward, tracker):
    if dice_roll(coward.init) > dice_roll(tracker.init):
        return True
    else:
        return False

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
