from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


c = Card("A", "hearts")
c1 = Card("10", "diamonds")
print(c)
print(c1)


class Deck:
    def __init__(self):
        suits = ["hearts", "diamonds", "clubs", "spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        if count == 0:
            raise ValueError("all cards have been dealt")
        actual = min(count, num)
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("only deck can be shuffled")
        shuffle(self.cards)
        return self


d = Deck()
d.shuffle()
hand = d.deal_hand(5)
print(hand)
