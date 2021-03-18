import poker
import Player


# 排序规则-先根据花色再根据点数排序
def get_key(card):
    return (card.suite, card.face)
if  __name__=='__main__':
    p = poker.Poker()
    p.shuffle()
    players = [Player.Player('东邪'), Player.Player('西毒'), Player.Player('南帝'), Player.Player('北丐')]
    for _ in range(13):
        for player in players:
            player.get(p.next)
    for player in players:
        print(player.name + ':', end=' ')
        player.arrange(get_key)
        for card in player.cards_on_hand:
            print(card, end=' ')
        print()
