from __future__ import annotations


class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other: Card):
        return self.rank == other.rank and self.suit == other.suit


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position: int):
        return self._cards[position]
