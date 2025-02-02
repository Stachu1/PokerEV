import time as t, random as rnd
from Player import Player
from Game import Game
from colorama import Fore, init
init()


num_other_players = int(input("Number players: ")) - 1


while True:
    print("")
    hand_input = input("Hand: ")
    hand = hand_input.split(" ") if len(hand_input) > 0 else hand
    community_cards_input = input("Community cards: ")
    community_cards = community_cards_input.split(" ") if community_cards_input != "" else []

    player = Player(hand)
    game = Game(player, num_other_players=num_other_players, community_cards=community_cards)
    
    for _ in range(100000):
        game.run()
        if _ % 1000 == 0:
            print(player, end="\r")
    print(player)