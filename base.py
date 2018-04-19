from copy import copy

from card_define import NUMBER


class WinAlgorithm(object):
    """普通算法 3N + 2"""

    def __init__(self, raw=False):
        self.stack = []  # 牌组栈
        self.cards = []  # 剩余手牌
        self.pairs = 0  # 将对个数
        self.raw = raw  # 是否直接返牌组栈

    def clear(self, raw=False):
        self.stack = []  # 牌组栈
        self.cards = []  # 剩余手牌
        self.pairs = 0  # 将对个数
        self.raw = raw  # 是否直接返牌组栈

    def start(self, cards):
        self.cards = copy(cards)
        self.cards.sort()

        if self.try_win():
            if self.raw:
                # 直接返回牌组栈
                return self.stack
            else:
                # 返回胡牌的排列
                win_cards = []
                for i in self.stack:
                    win_cards.extend(i)
                return win_cards
        else:
            return []

    def push(self, group):
        # 将牌组压栈
        self.stack.append(group)

    def roll_back(self):
        # 牌组出栈
        group = self.stack.pop()
        self.cards.extend(group)
        self.cards.sort()

    def try_triplets(self, card):
        # 尝试组成一个刻子，如果可以的话则将此组牌压栈
        if self.cards.count(card) >= 3:
            self.cards.remove(card)
            self.cards.remove(card)
            self.cards.remove(card)
            self.push([card, card, card])
            return True
        else:
            return False

    def try_sequence(self, card):
        if card not in NUMBER:
            return False
        # 尝试组成一个顺子，如果可以的话则将此组牌压栈
        if card in self.cards and card + 1 in self.cards and card + 2 in self.cards:
            self.cards.remove(card)
            self.cards.remove(card + 1)
            self.cards.remove(card + 2)
            self.push([card, card + 1, card + 2])
            return True
        else:
            return False

    def try_pair(self, card):
        # 尝试组成一个对子，对子只能有一个
        if self.pairs == 1:
            return False
        if self.cards.count(card) >= 2:
            self.cards.remove(card)
            self.cards.remove(card)
            self.push([card, card])
            self.pairs = 1
            return True
        else:
            return False

    def try_win(self):
        # 回溯尝试组成顺子刻子对子
        if not self.cards:
            if self.pairs == 1:
                return True
            else:
                return False

        active_card = self.cards[0]

        if self.try_triplets(active_card):
            if not self.try_win():
                self.roll_back()
            else:
                return True

        if self.try_pair(active_card):
            if not self.try_win():
                self.roll_back()
                self.pairs = 0
            else:
                return True

        if self.try_sequence(active_card):
            if not self.try_win():
                self.roll_back()
            else:
                return True

        return False


class WinAlgorithmSevenPairs(WinAlgorithm):
    """七对的胡牌算法"""

    def try_pair(self, card):
        if self.cards.count(card) >= 2:
            self.cards.remove(card)
            self.cards.remove(card)
            self.push([card, card])
            self.pairs += 1
            return True
        else:
            return False

    def try_win(self):
        if not self.cards and self.pairs == 7:
            return True

        active_card = self.cards[0]

        if self.try_pair(active_card):
            if not self.try_win():
                self.roll_back()
                self.pairs -= 1
            else:
                return True
        return False
