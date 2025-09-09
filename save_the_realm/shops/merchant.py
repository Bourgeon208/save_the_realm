store = {
    "Supply" : 50,
    "Sword" : 50,
    "Chainmail" : 80,
    "Potion" : 50,
    "Ellixir of life" : 400,
}

def merchant(player):
    print("You encounter a friendly Merchant, he proposes to trade.")
    print("(͡• ͜ʖ ͡•)")

    indexed_store = {str(i): item for i, item in enumerate(store, 1)}
    for i, item in indexed_store.items():
        print(i, item.ljust(17), str(store[item]).ljust(3), "gold")
    print("9 Leave the shop")

    while True:
        inp = input("What to do ? ")

        if inp in indexed_store:
            player.buy_item(indexed_store[inp])
        elif inp == "9":
            break
        else:
            print("Invalid choice.")
            

def buy_item(player, item):
    if not buy_check(player, item):
        return

    if item == "Sword":
        print("You bought a sword.")
        player.dmg_dice = (1,10)
        player.sword = True

    if item == "Armor":
        print("You bought an armor.")
        player.ac += 2
        player.armor = True

    if item == "Potion":
        print("You bought a potion.")
        player.hp = player.max_hp
        player.gold -= 50

    if item == "Elixir of life":
        if player.gold < 400:
            print("You don't have enough gold.")
        else:
            print("You bought and drink a potion.")
            # player.max_hp = player.max_hp + dice_roll(dice=(2,12))
            player.hp = player.max_hp
            player.gold -= 400

def buy_check(player, item):
    if player.item == True and item in ["Sword", "Chainmail"]:
        print(f"You already have {item}.")
        return False
    elif player.gold < store[item]:
        print("You don't have enough gold.")
        return False
    player.gold -= store[item]
    return True

merchant("")