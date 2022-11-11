import random


class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()


if __name__ == '__main__':
    # card = Card("Diamond", 5)
    # card.show()

    deck = Deck()
    deck.shuffle()
    deck.show()

    player = Player("Zap")
    player.draw(deck).draw(deck)
    player.show_hand()

    card = deck.draw_card()
    card.show()

    for i in range(3):
        player.draw(deck)

    print(f'\nThe {len(player.hand)} cards in {player.name}\'s hand:')
    player.show_hand()

    print('\nDiscarded:')
    player.discard().show()

    print(f'\nThe {len(player.hand)} cards in {player.name}\'s hand received by 4 players:')
    player.show_hand()



