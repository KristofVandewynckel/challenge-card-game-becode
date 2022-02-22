from card import Card
import random


class Player:
    def __init__(self):
        turn_count = 0
        number_of_cards = 0
        self.cards = Card
        self.history = ""

    def play(self):
        played_card = random.choice(Card)
        print(Card.color, Card.icon, Card.value)
        
Player.play


class Deck:
     def __init__(self):
        self.cards = Card()
        pass
     def fill_deck():
       pass
