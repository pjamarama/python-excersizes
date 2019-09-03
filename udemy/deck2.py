from random import shuffle

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        values = (['A', '2', '3', '4', '5', '6',
            '7', '8', '9', '10', 'J', 'Q', 'K'])
        self.cards = [Card(value, suit) for value in \
        values for suit in suits]

    def __iter__(self):
        return iter(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, cards_in_deck):
        count = self.count()
        actual = min(cards_in_deck, count)
        if count == 0:
            raise ValueError('All cards have been dealt')
        hand = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return hand

    def shuf(self):
        cards_in_deck = self.count()
        if cards_in_deck < 52:
            return 'Only full decks can be shuffled'
        return shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, number_to_deal):
        return self._deal(number_to_deal)



d = Deck()
d.shuf()
for jug in d:
    print (jug)


# d.shuf()
# d.deal_hand(3)
# print(d)
# d.deal_hand(49)
# d.deal_card()
# print(d)