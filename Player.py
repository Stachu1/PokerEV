import time as t, random as rnd
from collections import Counter
from colorama import Fore, init
init()

# Mapping for card ranks
RANKS = "23456789TJQKA"
RANK_VALUES = {rank: index for index, rank in enumerate(RANKS, start=2)}

# Hand rank base values
HAND_RANKS = {
    "high_card": 0,
    "one_pair": 1,
    "two_pair": 2,
    "three_of_a_kind": 3,
    "straight": 4,
    "flush": 5,
    "full_house": 6,
    "four_of_a_kind": 7,
    "straight_flush": 8,
    "royal_flush": 9
}


class Player:
    def __init__(self, hand=None):
        self.hand = hand
        self.wins = 0
        self.ties = 0
        self.losses = 0
    
    
    def __str__(self):
        games = self.wins + self.ties + self.losses
        return f"No gmaes played yet" if games == 0 else f"WR: {100*self.wins/games:.0f}% ({100*self.ties/games:.0f}%)   "
    
    
    def get_score(self, community_cards):
        cards = self.hand + community_cards
        hand_type, main_value, kickers = self.classify_hand(cards)
        score = HAND_RANKS[hand_type] * 100 + main_value * 7
        score += sum(k * (0.7 * 10 ** (-i)) for i, k in enumerate(kickers))  # Kickers for tie-breakers
        return score
    
    
    def classify_hand(self, cards):
        parsed_cards = self.parse_cards(cards)
        ranks = [r for r, s in parsed_cards]
        suits = [s for r, s in parsed_cards]
        rank_counts = self.get_rank_counts(parsed_cards)
        counts = sorted(rank_counts.values(), reverse=True)
        unique_ranks = sorted((RANK_VALUES[r] for r in rank_counts), reverse=True)

        flush, flush_ranks = self.is_flush(parsed_cards)
        straight, high_straight = self.is_straight(ranks)

        if flush and straight:
            if high_straight == 14:  # Royal Flush
                return ("royal_flush", 14, [])
            return ("straight_flush", high_straight, [])
        if counts[0] == 4:
            quad_rank = RANK_VALUES[[r for r in rank_counts if rank_counts[r] == 4][0]]
            kicker = max(r for r in unique_ranks if r != quad_rank)
            return ("four_of_a_kind", quad_rank, [kicker])
        if counts[0] == 3 and counts[1] >= 2:
            set_rank = RANK_VALUES[[r for r in rank_counts if rank_counts[r] == 3][0]]
            pair_rank = max(RANK_VALUES[r] for r in rank_counts if rank_counts[r] >= 2 and RANK_VALUES[r] != set_rank)
            return ("full_house", set_rank, [pair_rank])
        if flush:
            return ("flush", max(flush_ranks), flush_ranks)
        if straight:
            return ("straight", high_straight, [])
        if counts[0] == 3:
            set_rank = RANK_VALUES[[r for r in rank_counts if rank_counts[r] == 3][0]]
            kickers = sorted((r for r in unique_ranks if r != set_rank), reverse=True)[:2]
            return ("three_of_a_kind", set_rank, kickers)
        if counts[0] == 2 and counts[1] == 2:
            pair_ranks = sorted((RANK_VALUES[r] for r in rank_counts if rank_counts[r] == 2), reverse=True)
            kicker = max(r for r in unique_ranks if r not in pair_ranks)
            return ("two_pair", pair_ranks[0], [pair_ranks[1], kicker])
        if counts[0] == 2:
            pair_rank = RANK_VALUES[[r for r in rank_counts if rank_counts[r] == 2][0]]
            kickers = sorted((r for r in unique_ranks if r != pair_rank), reverse=True)[:3]
            return ("one_pair", pair_rank, kickers)

        return ("high_card", max(unique_ranks), unique_ranks[:5])
    
    
    def parse_cards(self, cards):
        return [(card[0], card[1]) for card in cards]  # (rank, suit)


    def get_rank_counts(self, cards):
        ranks = [card[0] for card in cards]
        return Counter(ranks)


    def is_flush(self, cards):
        suits = [card[1] for card in cards]
        suit_counts = Counter(suits)
        for suit, count in suit_counts.items():
            if count >= 5:
                flush_cards = sorted([card for card in cards if card[1] == suit], key=lambda x: RANK_VALUES[x[0]], reverse=True)
                flush_ranks = [RANK_VALUES[card[0]] for card in flush_cards[:5]]
                return True, flush_ranks
        return False, []


    def is_straight(self, ranks):
        rank_indices = sorted(set(RANK_VALUES[rank] for rank in ranks), reverse=True)
        if len(rank_indices) < 5:
            return False, None

        # Check for standard straight
        for i in range(len(rank_indices) - 4):
            if rank_indices[i + 4] - rank_indices[i] == 4:
                return True, rank_indices[i]

        # Special case: A-2-3-4-5
        if set([14, 2, 3, 4, 5]).issubset(rank_indices):
            return True, 5

        return False, None