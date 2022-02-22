from card import Card
from random import choice
from random import shuffle


class Player:
    def __init__(self, name:str):
        self.name = name
        self.turn_count = 0
        self.number_of_cards = 0
        self.cards = []
        self.history = []

    def play(self):
        played_card = choice(self.cards)
        print(played_card)
        self.history.append(played_card)
        self.turn_count+=1
        print(f"{self.name},{self.turn_count} played {played_card}")
        self.cards.remove(played_card)
        
class Deck:
    def __init__(self):
        self.cards = []
    def fill_deck(self):
        for i in Card.icon:
            for v in Card.value:
                self.cards.append(v+i)

    def shuffle(self):
        shuffle(self.cards)       
        
    def distribute (self, n_players):
            number_of_cards = int(52 // n_players)
            print(number_of_cards)
            
            for each in range (0,n_players):
                for hand in range(0,number_of_cards):
                    picked_card = choice(self.cards)
                    self.cards += picked_card
                    self.cards.remove(picked_card)
                print(self.cards)
                
#            for i in range(0,n_players):
#                for j in range(0, number_of_cards):
#                    i.cards += [self.cards[0]]
#                    self.cards.remove(self.cards[0])



"""        number_of_cards = int(52 / len(n_players))
        for player in n_players:
            for cards in range(0,number_of_cards):
                player.cards +=[self.cards[0]]
                self.cards.remove(self.cards[0])
                print(self.cards)"""
        
deck = Deck()

deck.fill_deck()
deck.shuffle()
deck.distribute(3)


"""def distribute (self, n_players):
        number_of_cards = int(52 / len(n_players))
        for i in n_players:
            for j in range(0, number_of_cards):
                i.cards += [self.cards[0]]
                self.cards.remove(self.cards[0])"""
