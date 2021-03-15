from Card import Card
from random import *


class Poker(object):
    #一副牌
    def __init__(self):
        self._cards = []
        self._current = 0
        for suite in range(4):
            for face in range(1, 14):
                card = Card(suite, face)
                self._cards.append(card)

    @property
    def cards(self):
        return self.cards

    def shuffle(self):
        self._current = 0
        cards_len = len(self._cards)
        for index in range(cards_len):
            pos = randrange(cards_len)
            self._cards[index], self._cards[pos] = self._cards[
                pos], self._cards[index]

    @property
    def next(self):
        #发牌
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        #还有没有牌
        return self._current < len(self._cards)
