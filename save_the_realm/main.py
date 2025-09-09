import time
from characters import player, monster, friend
from maps import labyrinth, movement, event
from combats import encounter

map = labyrinth
print("Greetings adventurer, the king asked of you to kill a Dragon resting in the labyrinth full of monsters.")
name = input("What is your name ?")
# player_1 = player.Player(name, 10, 2, (1,6), 2, 2, 12, 0, 0)
player_1 = player.Player(name, 100, 20, (100,600), 200, 20, 120, 0, 0)
print("Controls are ZQSD to move. \nC to see character's stats. \nR to rest.")


def handle_encounter(new_pos, player, game_state):
    if new_pos not in monster.monster_map:
        return None

    cls, after = monster.monster_map[new_pos]
    enemy = cls()
    result = encounter.Encounter(enemy, player).combat()

    if after:
        after(result, game_state)

    return result

def move():
    game_state["map"][player_line][player_col] = " "
    game_state["map"][new_player_line][new_player_col] = "X"

game_state = {"map": map, "player_line": 1, "player_col": 1}

while player_1.hp > 0:
    new_player_line, new_player_col, player_line, player_col = movement(game_state["map"], player_1)
    new_pos = game_state["map"][new_player_line][new_player_col]

    if new_pos in ["▌", "▐", "█", "▀", "▄"]:
        print("You can't go that way !")
        time.sleep(1)

    elif new_pos == " ":
        move()

    elif new_pos == "U":
        friend.unicorn(player_1)
        encounter_result = True

    elif new_pos == "S":
        print("You encounter a friendly Merchant, he proposes to trade.")
        print("(͡• ͜ʖ ͡•)")
        print("a) Sword (50 gold), b) Armor (80 gold), c) Potion (50 gold), d) Elixir of life (400 gold), e) Leave the shop")
        while True:
            inp = input("What to do ?").lower()
            if inp == "a":
                player_1.buy_item("Sword")
            elif inp == "b":
                player_1.buy_item("Armor")
            elif inp == "c":
                player_1.buy_item("Potion")
            elif inp == "d":
                player_1.buy_item("Elixir of life")
            elif inp == "e":
                break

    elif new_pos == "H":
        event.human()
        move()

    else:
        encounter_result = handle_encounter(new_pos, player_1, game_state)

        if new_pos == "K" and encounter_result:
            event.credits(player_1)
            break

        if encounter_result:
            move()

if player_1.hp < 1:
    event.death()
