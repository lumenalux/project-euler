"""
In the game, Monopoly, the standard board is set up in the following way:

        GO   A1   CC1  A2   T1   R1   B1   CH1  B2   B3   JAIL

        H2                                                C1

        T2                                                U1

        H1                                                C2

        CH3                                               C3

        R4                                                R2

        G3                                                D1

        CC3                                               CC2

        G2                                                D2

        G1                                                D3

        G2J  F3   U2   F2   F1   R3   E3   E2   CH2  E1   FP

A player starts on the GO square and adds the scores on two 6-sided dice to
determine the number of squares they advance in a clockwise direction.
Without any further rules we would expect to visit each square with equal
probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest),
and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the
player to go directly to jail, if a player rolls three consecutive doubles,
they do not advance the result of their 3rd roll. Instead they proceed
directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player
lands on CC or CH they take a card from the top of the respective pile and,
after following the instructions, it is returned to the bottom of the pile.
There are sixteen cards in each pile, but for the purpose of this problem we
are only concerned with the top two cards in each pile.

    * Community Chest (2/16 cards):
        1. Advance to GO
        2. Go to JAIL

    * Chance (10/16 cards):
        1. Advance to GO
        2. Go to JAIL
        3. Go to C1
        4. Go to E3
        5. Go to H2
        6. Go to R1
        7. Go to next R (railway company)
        8. Go to next R
        9. Go to next U (utility company)
        10. Go back 3 squares

The heart of this problem concerns the likelihood of visiting a particular
square. That is, the probability of finishing at that square after a roll.
For this reason it should be clear that, with the exception of G2J for which
the probability of finishing on it is zero, the CH squares will have the lowest
probabilities, as 5/8 request a movement to another square, and it is the
final square that the player finishes at on each roll that we are interested
in.

We shall make no distinction between "Just Visiting" and being sent to JAIL,
and we shall also ignore the rule about requiring a double to
"get out of jail", assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can
concatenate these two-digit numbers to produce strings that correspond with
sets of squares.

Statistically it can be shown that the three most popular squares, in order,
are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and
GO (3.09%) = Square 00. So these three most popular squares can be listed
with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the
six-digit modal string.

link: https://projecteuler.net/problem=84

Solution:

The method used to solve this problem is a Monte Carlo simulation, which is a
computational technique that relies on repeated random sampling to obtain
numerical results. Specifically, for the Monopoly game simulation, the method
involves simulating the roll of dice and movement around the Monopoly board
numerous times to statistically determine the probability of landing on each
square.

The simulation involves rolling two 4-sided dice to mimic the possible
outcomes when a player rolls dice in Monopoly. Each roll determines how many
spaces the player moves forward on the board.

The player's position on the board is updated based on the dice roll, moving
them forward the sum of the dice rolls. The board is treated as a circular
track, so if the player's movement goes past the last square, it wraps
around to the beginning.

Certain squares on the Monopoly board have special rules. For instance,
landing on the "Go to Jail" square sends the player directly to Jail,
bypassing the normal movement rules. Community Chest (CC) and Chance (CH)
squares can alter the player's position based on the drawn card from the
respective decks. Only cards that affect movement are considered in this
simulation.

If the player rolls doubles (both dice have the same value), they get to
roll again. However, rolling doubles three times in a row sends the player
directly to Jail. The simulation keeps track of consecutive doubles to
enforce this rule.

Each time the player lands on a square, that event is recorded. The simulation
runs for a large number of turns to ensure a statistically significant sample
size. After many turns, the frequency of landing on each square is analyzed to
determine the most visited squares.

The squares are ranked by how frequently players land on them. The most
visited squares are identified, and their board positions are used to create a
six-digit modal string, representing the solution to the problem.
"""
import random

from dataclasses import dataclass, field
from collections import defaultdict
from itertools import repeat


@dataclass
class MonopolySimulation:
    seed: int = 220
    dice_sides: int = 4  # Using 4-sided dice by default
    board_size: int = 40
    go: int = 0
    jail: int = 10
    g2j: int = 30
    cc_squares: list = field(default_factory=lambda: [2, 17, 33])
    ch_squares: list = field(default_factory=lambda: [7, 22, 36])

    # GO, JAIL and others are None
    cc_cards: list = field(default_factory=lambda: [0, 10] + [None] * 14)

    @staticmethod
    def _default_ch_cards_factory():
        return [
            0, 10, 11, 24, 39, 5,
            'next_r', 'next_r', 'next_u', 'back_3',
            *repeat(None, 6)
        ]
    ch_cards: list = field(default_factory=_default_ch_cards_factory)

    position_counts: dict = field(default_factory=lambda: defaultdict(int))
    position: int = 0
    doubles_count: int = 0
    num_turns: int = 1_000_000

    def roll_dice(self):
        return (
            random.randint(1, self.dice_sides),
            random.randint(1, self.dice_sides)
        )

    def move_position(self, roll):
        self.position = (self.position + sum(roll)) % self.board_size

    def handle_special_squares(self):
        if self.position in self.cc_squares:
            card = random.choice(self.cc_cards)
            if card is not None:
                self.position = card
                return

        if self.position in self.ch_squares:
            card = random.choice(self.ch_cards)
            if card is not None:
                if isinstance(card, str):
                    self.handle_card_actions(card)
                else:
                    self.position = card
                return

        if self.position == self.g2j:
            self.position = self.jail

    def handle_card_actions(self, card):
        if card == 'next_r':
            next_r = [5, 15, 25, 35]
            self.position = next((r for r in next_r if r > self.position), 5)
        elif card == 'next_u':
            self.position = 28
            if self.position < 12 or self.position >= 28:
                self.position = 12
        elif card == 'back_3':
            self.position = (self.position - 3) % self.board_size

    def simulate_turn(self):
        roll = self.roll_dice()
        if roll[0] == roll[1]:
            self.doubles_count += 1
        else:
            self.doubles_count = 0  # Reset doubles count if not a double

        if self.doubles_count == 3:
            self.position = self.jail
            self.doubles_count = 0
            return
        self.move_position(roll)
        self.handle_special_squares()

    def run_simulation(self):
        random.seed(self.seed)
        for _ in range(self.num_turns):
            self.simulate_turn()
            self.position_counts[self.position] += 1

        # Find the most popular squares
        most_popular = sorted(self.position_counts,
                              key=self.position_counts.get, reverse=True)[:3]
        return ''.join([str(square).zfill(2) for square in most_popular])


def solution(dice_sides, num_turns=1_000_000):
    simulation = MonopolySimulation(
        dice_sides=dice_sides,
        num_turns=num_turns
    )
    modal_string = simulation.run_simulation()
    return modal_string


if __name__ == '__main__':
    print(solution(6))  # 102400
    print(solution(4))  # 101524
