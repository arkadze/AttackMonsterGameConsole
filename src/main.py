import sys
import os
import random

sys.path.insert(0, os.path.dirname(__file__))

from entities import Player, Potion, Monster
from core import Config


def monster_killed(monster: Monster, player: Player):
    player.add_gold(monster.gold)
    player.level_up()

    print(f"You killed the {monster.name}.")
    print(f"You are now level {player.level}.")
    print(f"You found {monster.gold} gold.")

    if random.randint(1, 100) <= Config.POTION_CHANCE:
        potion = Potion.get_random_potion()

        print("You found a mythical potion! Do you want to drink it? [y/n]: ")
        answer = input().strip().lower()

        if answer == 'y':
            player.drink_potion(potion)
            print(f"You drank a {potion.get_size_name()} potion of {potion.get_name()}.")

def attack_monster(monster: Monster, player: Player):
    # if player.is_dead(): return

    monster.reduce_health(player.damage)
    print(f"You hit the {monster.name} for {player.damage} damage.")

    if monster.is_dead(): monster_killed(monster, player)

def attack_player(player: Player, monster: Monster):
    if monster.is_dead(): return

    player.reduce_health(monster.damage)
    print(f"The {monster.name} hit you for {monster.damage} damage.")

def fight_monster(player: Player):
    monster = Monster.get_random_monster()
    print(f"You have encountered a {monster.name} ({monster.symbol}).")

    while not monster.is_dead() and not player.is_dead():
        print(f"(R)un, (F)ight or (S)pecifications: ")
        answer = input().strip().lower()

        match answer:
            case 's':
                print(player)
            case 'r':
                if random.randint(1, 100) <= Config.FLEE_SUCCESS_CHANCE:
                    print("You failed to flee.")
                    attack_player(player, monster)
                else:
                    print("You successfully fled.")
                    return
            case 'f':
                attack_monster(monster, player)
                attack_player(player, monster)


def main():
    name = input("Enter your name: ").strip()
    player = Player(name)

    while not (player.has_won() or player.is_dead()):
        fight_monster(player)

    if player.is_dead():
        print(f"You died at level {player.level} and with {player.gold} gold!")
        print(f"Too bad you can’t take it with you!")
    elif player.has_won():
        print(f"You won the game with {player.gold} gold!")


if __name__ == "__main__":
    main()
