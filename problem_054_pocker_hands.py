"""
In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

    * High Card: Highest value card.
    * One Pair: Two cards of the same value.
    * Two Pairs: Two different pairs.
    * Three of a Kind: Three cards of the same value.
    * Straight: All cards are consecutive values.
    * Flush: All cards of the same suit.
    * Full House: Three of a kind and a pair.
    * Four of a Kind: Four cards of the same value.
    * Straight Flush: All cards are consecutive values of same suit.
    * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:

    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

    Hand    Player 1            Player 2            Winner
    1       5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
            Pair of Fives       Pair of Eights

    2       5D 8C 9S JS AC      2C 5C 7D 8S QH      Player 1
            Highest card Ace    Highest card Queen

    3       2D 9C AS AH AC      3D 6D 7D TD QD      Player 2
            Three Aces          Flush with Diamonds

    4       4D 6S 9H QH QC      3D 6D 7H QD QS      Player 1
            Pair of Queens      Pair of Queens
            Highest card Nine   Highest card Seven

    5       2H 2D 4C 4D 4S      3C 3D 3S 9S 9D      Player 1
            Full House          Full House
            With Three Fours    with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each
player's hand is in no specific order, and in each hand there is a clear
winner.

How many hands does Player 1 win?
"""
from collections import Counter
from itertools import pairwise


class Card:
    VALUE_MAP = {k: v+2 for v, k in enumerate('23456789TJQKA')}
    SUIT_MAP = {k: v for v, k in enumerate('CDHS')}

    def __init__(self, card_string):
        self.value = self.VALUE_MAP[card_string[0]]
        self.suite = self.SUIT_MAP[card_string[1]]

    def __lt__(self, other):
        return self.value < other.value


class Hand:
    def __init__(self, hand_string):
        self.cards = tuple(sorted(map(Card, hand_string.split())))
        self.value_count = Counter(card.value for card in self.cards)

    def is_straight_flush(self):
        return self.is_flush() and self.is_straight()

    def is_four_of_a_kind(self):
        return any(count == 4 for count in self.value_count.values())

    def is_full_house(self):
        return self.is_three_of_a_kind() and self.is_one_pair()

    def is_flush(self):
        suite_count = Counter(card.suite for card in self.cards)
        return any(count == 5 for count in suite_count.values())

    def is_straight(self):
        return all(a.value + 1 == b.value for a, b in pairwise(self.cards))

    def is_three_of_a_kind(self):
        return any(count == 3 for count in self.value_count.values())

    def is_two_pairs(self):
        return sum(count == 2 for count in self.value_count.values()) == 2

    def is_one_pair(self):
        return any(count == 2 for count in self.value_count.values())

    def __lt__(self, other):
        hand_a, hand_b = ((hand.is_straight_flush() * hand.cards or (0,) * 5,

                           hand.cards[1].value
                           if hand.is_four_of_a_kind() else 0,

                           hand.is_full_house(),

                           hand.is_flush(),

                           tuple(card.value for card in hand.cards)
                           if hand.is_straight() else (0,) * 5,

                           hand.cards[2].value
                           if hand.is_three_of_a_kind() else 0,

                           (hand.cards[1].value, hand.cards[3].value)
                           if hand.is_two_pairs() else (0, 0),

                           next(k for k, v in hand.value_count.items()
                                if v == 2) if hand.is_one_pair() else 0,

                           max((k for k, v in hand.value_count.items()
                                if v == 1), default=0),
                           ) for hand in (self, other))

        return hand_a < hand_b


def solution():
    with open('resources/0054_poker.txt') as f:
        games = ((g[:14], g[15:29]) for g in (line for line in f))
        return sum(Hand(hand_a) > Hand(hand_b) for hand_a, hand_b in games)


# test
if __name__ == '__main__':
    print(Hand('5H 5C 6S 7S KD') > Hand('2C 3S 8S 8D TD'))  # False
    print(Hand('5D 8C 9S JS AC') > Hand('2C 5C 7D 8S QH'))  # True
    print(Hand('2D 9C AS AH AC') > Hand('3D 6D 7D TD QD'))  # False
    print(Hand('4D 6S 9H QH QC') > Hand('3D 6D 7H QD QS'))  # True
    print(Hand('2H 2D 4C 4D 4S') > Hand('3C 3D 3S 9S 9D'))  # True

    print(solution())  # 376
