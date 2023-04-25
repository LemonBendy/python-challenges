import random

class player():
    def __init__(self, name):
        self.__name = name
        self.__score = 0
        self.__hand = []

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_hand(self):
        return self.__hand

    def set_name(self, name):
        self.__name = name

    def hit(self, card):
        self.__hand.append(card)
        self.__score += card.get_value()

    def stand(self):
        pass

    def bust(self):
        self.__score > 21

    def win(self):
        self.__score == 21

class dealer(player):
    def __init__(self):
        self.__name = 'Dealer'
        self.__score = 0
        self.__hand = []

    def deal(self):
        pass

class deck():
    def __init__(self):
        self.__cards = []
        self.__suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.__values = [1,2,3,4,5,6,7,8,9,10,10,10,10]
        self.__ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        for suit in self.__suits:
            for value in self.__values:
                for rank in self.__ranks:
                    self.__cards.append(card(suit, value, rank))

    def get_cards(self):
        return self.__cards

    def get_suits(self):
        return self.__suits

    def get_values(self):
        return self.__values
    


    def shuffle(self):
        random.shuffle(self.__cards)

    def deal(self):
        pass

class card():
    def __init__(self, suit, value, rank):
        self.__suit = suit
        self.__value = value
        self.__rank = rank

    def get_suit(self):
        return self.__suit

    def get_value(self):
        return self.__value

    def get_rank(self):
        return self.__rank
