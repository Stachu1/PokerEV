import time as t, random as rnd
from Player import Player
from Game import Game
from colorama import Fore, init
init()


num_other_players = int(input(f"{Fore.MAGENTA}Number players: {Fore.RESET}")) - 1


try:
    while True:
        print(f"{Fore.BLUE}{"="*20}")
        hand_input = input(f"{Fore.CYAN}Hand(unchanged): {Fore.RESET}")
        hand = hand_input.split(" ") if len(hand_input) > 0 else hand
        community_cards_input = input(f"{Fore.CYAN}Community cards: {Fore.RESET}")
        community_cards = community_cards_input.split(" ") if community_cards_input != "" else []
        print("")

        player = Player(hand)
        game = Game(player, num_other_players=num_other_players, community_cards=community_cards)

        for _ in range(200000):
            game.run()
            if _ % 5000 == 0:
                print(player, end="\r")
        print(player)
except KeyboardInterrupt:
    print(f"\n{Fore.MAGENTA}Closing...{Fore.RESET}")
    exit(0)
except Exception as e:
    print(f"{Fore.RED}Error: {e}{Fore.RESET}")
    exit(1)
