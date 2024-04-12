# Make a 2 player Battle game, using Python!
#
# Player selects a character/fighter (from 4-6) or gets one assigned to them randomly.
#
# If Player 2, let them pick the character/fighter they want. If CPU assign a character/fighter randomly.
#
# The two characters need to fight.
#
# A winner must be declared via some sort of calculation.
#
# Bonus: Want to play again?
import random

player_1_attack = random.randint(5, 50)
player_1_defense = random.randint(1, 10)
player_1_health = random.randint(100, 200)

player1 = {
    'attack': player_1_attack,
    'defense': player_1_defense,
    'health': player_1_health
}

player_2_attack = random.randint(5, 50)
player_2_defense = random.randint(1, 10)
player_2_health = random.randint(100, 200)

player2 = {
    'attack': player_2_attack,
    'defense': player_2_defense,
    'health': player_2_health
}


def play_again():
    j = int(input("type 1 to play again"))
    if j == 1:
        player_1_attack = random.randint(5, 50)
        player_1_defense = random.randint(1, 10)
        player_1_health = random.randint(100, 200)

        player1 = {
            'attack': player_1_attack,
            'defense': player_1_defense,
            'health': player_1_health
        }

        player_2_attack = random.randint(5, 50)
        player_2_defense = random.randint(1, 10)
        player_2_health = random.randint(100, 200)

        player2 = {
            'attack': player_2_attack,
            'defense': player_2_defense,
            'health': player_2_health
        }

        battle(player1, player2)
    else:
        print("Good game")


def battle(player, player_2):
    print(
        f"Player 1, your stats are: \n Attack: {player['attack']}, Defense: {player['defense']}, Health: {player['health']}")
    print(
        f"Player 2, your stats are: \n Attack: {player_2['attack']}, Defense: {player_2['defense']}, Health: {player_2['health']}\n")
    coinflip = random.randint(0, 1)
    first_attacker = True
    if coinflip == 0:
        print("Player 1 has been selected to attack first")
    else:
        print("Player 2 has been selected to attack first")
        first_attacker = False
    battle_turn = 0
    battle_active = True
    while battle_active:

        player1_initial_health = player['health']
        player2_initial_health = player_2['health']

        print(f"\nTurn {battle_turn + 1}")
        print(
            f"Player 1 Stats \n Attack: {player['attack']}, Defense: {player['defense']}, Health: {player['health']}")
        print(
            f"Player 2 Stats \n Attack: {player_2['attack']}, Defense: {player_2['defense']}, Health: {player_2['health']}")
        if int(player['health']) <= 0:
            print(f"\nPlayer 2 has won the battle in {battle_turn} turns")
            battle_active = False
        elif int(player_2['health']) <= 0:
            print(f"\nPlayer 1 has won the battle in {battle_turn} turns")
            battle_active = False
        else:
            battle_turn = battle_turn + 1
            if first_attacker:  # player 1 hits player 2 first
                player_2['health'] = player_2['health'] - (player['attack'] - player_2['defense'])
                player['health'] = player['health'] - (player_2['attack'] - player_2['defense'])

                if player['health'] >= player1_initial_health:  # resets health if it goes over original health
                    player['health'] = player1_initial_health
                if player_2['health'] >= player2_initial_health:
                    player_2['health'] = player2_initial_health

                if int(player['health']) <= 0:  # sets health to 0 if it goes below 0 so that in final stats it
                    player['health'] = 0  # that health is 0 instead of a negative
                elif int(player_2['health']) <= 0:
                    player_2['health'] = 0
                    if player['health'] == player_2['health']:
                        player['health'] = 1
                        print("Player 1 just barely survived")

            else:  # player 2 hits player 1 first
                player['health'] = player['health'] - (player_2['attack'] - player_2['defense'])
                player_2['health'] = player_2['health'] - (player['attack'] - player_2['defense'])

                if player['health'] >= player1_initial_health:  # resets health if it goes over original health
                    player['health'] = player1_initial_health
                if player_2['health'] >= player2_initial_health:
                    player_2['health'] = player2_initial_health

                if int(player['health']) <= 0:  # sets health to 0 if it goes below 0 so that in final stats it
                    player['health'] = 0  # that health is 0 instead of a negative
                elif int(player_2['health']) <= 0:
                    player_2['health'] = 0
                    if player_2['health'] == player['health']:
                        player_2['health'] = 1
                        print("Player 2 just barely survived")
    play_again()


battle(player1, player2)
play_again()
