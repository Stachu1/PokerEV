import time as t, random as rnd
from Player import Player
from colorama import Fore, init
init()



DECK = ["2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "Tc", "Jc", "Qc", "Kc", "Ac",
        "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "Td", "Jd", "Qd", "Kd", "Ad",
        "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "Th", "Jh", "Qh", "Kh", "Ah",
        "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "Ts", "Js", "Qs", "Ks", "As"]

CLUBS = "♣️"
DIMONDS = "♦️"
HEARTS = "♥️"
SPADES = "♠️"


class Game:
    def __init__(self, player, num_other_players=1, community_cards=[]):
        self.player = player
        self.num_other_players = num_other_players
        self.community_cards = community_cards
    
    
    def deal_community_cards(self):
        deck = DECK.copy()
        deck = list(set(deck) - set(self.community_cards) - set(self.player.hand))
        rnd.shuffle(deck)
        community_cards = self.community_cards.copy()
        community_cards += deck[:5 - len(self.community_cards)]
        return community_cards
    
    
    def run(self):
        community_cards = self.deal_community_cards()
        player_score = self.player.get_score(community_cards)
        
        deck = DECK.copy()
        deck = list(set(deck) - set(self.community_cards) - set(self.player.hand))
        rnd.shuffle(deck)
        
        other_players_score = max([Player(deck[2*i:2 + 2*i]).get_score(community_cards) for i in range(self.num_other_players)])
        
        if player_score > other_players_score:
            self.player.wins += 1
        elif player_score < other_players_score:
            self.player.losses += 1
        else:
            self.player.ties += 1