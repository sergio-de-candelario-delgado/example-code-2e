import pytest

from data_model.frenchdeck import FrenchDeck, Card


class FrenchDeckTest:
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(self, card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(self.suit_values) + self.suit_values[card.suit]

    @pytest.mark.parametrize(
        "card,card_rank_value_result,card_rank_value_final_result",
        [
            (Card("A", 'clubs'), 12, 48),
            (Card("A", 'diamonds'), 12, 49),
            (Card("A", 'hearts'), 12, 50),
            (Card("A", 'spades'), 12, 51),
            (Card("2", 'clubs'), 0, 0),
            (Card("2", 'diamonds'), 0, 1),
            (Card("2", 'hearts'), 0, 2),
            (Card("2", 'spades'), 0, 3),
        ],
    )
    def test_card_ranks(self, card: Card, card_rank_value_result: int, card_rank_value_final_result: int):
        card_rank_value = FrenchDeck.ranks.index(card.rank)
        card_rank_value_final = card_rank_value * len(self.suit_values) + self.suit_values[card.suit]

        assert card_rank_value == card_rank_value_result
        assert card_rank_value_final == card_rank_value_final_result

    @pytest.mark.parametrize(
        "reverse, card",
        [
            (False, Card("2", "clubs")),
            (True, Card("A", "spades")),
        ],
    )
    def test_sorted_cards_by_max_rank(self, reverse: bool, card: Card):
        deck = FrenchDeck()

        sorted_card = sorted(deck, key=self.spades_high, reverse=reverse)[0]

        assert sorted_card == card

    def test_length_of_the_deck(self):
        deck = FrenchDeck()

        assert len(deck) == 52

    @pytest.mark.parametrize(
        "suit",
        [
            "spades",
            "hearts",
            "diamonds",
            "clubs",
        ],
    )
    def test_filter_dictionary_by_suit(self, suit):
        deck = FrenchDeck()

        filtered_values = filter(lambda item: item.suit == suit, deck)

        assert len(list(filtered_values)) == 13

    @pytest.mark.parametrize(
        "rank",
        [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "K",
            "Q",
            "A",
        ],
    )
    def test_filter_dictionary_by_rank(self, rank):
        deck = FrenchDeck()

        filtered_values = filter(lambda item: item.rank == rank, deck)

        assert len(list(filtered_values)) == 4
