import pytest

from data_model.frenchdeck import FrenchDeck, Card


class FrenchDeckTest:

    @pytest.mark.parametrize(
        "card,card_rank_value_result,card_rank_value_final_result",
        [
            (Card("A", 'clubs'), 12, 48),
            (Card("A", 'diamonds'), 12, 49),
            (Card("A", 'hearts'), 12, 50),
            (Card("A", 'spades'), 12, 51),
        ],
    )
    def test_card_ranks(self, card: Card, card_rank_value_result: int, card_rank_value_final_result: int):
        suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

        card_rank_value = FrenchDeck.ranks.index(card.rank)
        card_rank_value_final = card_rank_value * len(suit_values) + suit_values[card.suit]

        assert card_rank_value == card_rank_value_result
        assert card_rank_value_final == card_rank_value_final_result
