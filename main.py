import time as t, random as rnd
from sys import argv
from Player import Player
from Game import Game
from colorama import Fore, init
init()

iterations = int(argv[1]) if len(argv) > 1 else 200000
num_other_players = int(input(f"{Fore.MAGENTA}Number players: {Fore.RESET}")) - 1


try:
    while True:
        print(f"{Fore.BLUE}{"="*22}")
        hand_input = input(f"{Fore.CYAN}Hand(unchanged): {Fore.RESET}")
        hand = hand_input.split(" ") if len(hand_input) > 0 else hand

        community_cards_input = input(f"{Fore.CYAN}Community cards: {Fore.RESET}")
        community_cards = community_cards_input.split(" ") if community_cards_input != "" else []

        player = Player(hand)
        game = Game(player, num_other_players=num_other_players, community_cards=community_cards)

        game.pot = int(input(f"{Fore.CYAN}Pot: {Fore.RESET}"))
        game.to_call = int(input(f"{Fore.CYAN}To call: {Fore.RESET}"))
        print("")

        try:
            for _ in range(iterations):
                game.run()
                if _ % 5000 == 0:
                    player.update_ev(game.pot, game.to_call)
                    print(player, end="\r")
        except KeyboardInterrupt:
            pass
        print("\33[2K", end="\r");
        print(player)

except KeyboardInterrupt:
    print(f"\n{Fore.MAGENTA}Closing...{Fore.RESET}")
    exit(0)

except Exception as e:
    print(f"{Fore.RED}Error: {e}{Fore.RESET}")
    exit(1)
