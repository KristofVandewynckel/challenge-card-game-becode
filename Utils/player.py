"""
We import the Card class and choice and shuffle from the random module.
"""

from card import Card
from random import choice
from random import shuffle

"""
We then create a class called Player which creates player objects with a name,
a turn counter, a hand of cards (that they can play) and a history of played
cards. The number_of_cards attribute can keep track of how many cards each 
player has left

What our player needs to do of course, is play a card. To do this in the play
method we can use aplayer's input but in this case we're picking a random card 
from their hand.
This is then played and our player's history gain one played card and their
turn counter goes up by one. Furthermore the played card has to be removed from
their hand.

"""
class Player:
    def __init__(self, name:str):
        self.name = name
        self.turn_count = 0
        self.number_of_cards = 0
        self.hand = []
        self.history = []

    def play(self):
        played_card = choice(self.hand)
        self.history.append(played_card)
        self.turn_count+=1
        print(f"{self.name}, in turn {self.turn_count} played {played_card}")
        self.hand.remove(played_card)

"""
Here we create a Deck class which will create a deck of 52 cards for us.

Fill deck will go through all the symbols and values per symbol we determined
in out Card class and create one of each to fill a deck with 52 cards.

The shuffle method will randomize this list of cards.

The distribute takes information from the start of our game (see game.py) and 
give each player their cards to their hand. This is done as evenly as possible.
Any cards left are not taking into the game or deck.

We do this by dividing the cards by the amount of players and then taking 
that range out of the shuffled deck to then place it into player's hands.
"""

class Deck:
    def __init__(self):
        self.cards = []
               
    def fill_deck(self):
        for i in Card.icon:
            for v in Card.value:
                self.cards.append(v+i)

    def shuffle(self):
        shuffle(self.cards)     
        
    def distribute (self, n_players,player_list):
            number_of_cards = int(52 // n_players)
            for each in player_list:
                each.hand += self.cards[0:number_of_cards]
                del self.cards[0:number_of_cards]


                
    
