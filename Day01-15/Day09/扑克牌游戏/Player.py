from Card import *

class Player(object):
    #玩家
    def __init__(self,name):
        self._name=name
        self._cards_on_hand=[]
    
    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand
    def get(self,card):
        #摸排
        self._cards_on_hand.append(card)

    def arrange(self,card_key):
        #玩家整理手上的牌
        self._cards_on_hand.sort(key=card_key)
    
    def get_key(card):
        # 排序规则-先根据花色再根据点数排序
        return(card.suite,card.face)
