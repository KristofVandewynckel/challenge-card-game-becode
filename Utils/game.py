""" We import the Deck and Player class"""

from player import Deck
from player import Player

"""
This creates the board we play on. When the game starts with the start_game 
method. We first ask the number of players and their names. This information
is used by our distribute method (see player.py) to divide the cards.

Once this is done, we create a playing field to then loop over the player's
hand. As long as cards are remaining, they have to keep playing a card a turn.
The turn counter moves one up after all players have played a card.

The played cards are shown in the active_cards list but move to the history as
soon as new cards are about to be played.
"""

class Board:
    def __init__(self):
        self.players = []
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []
        
    def start_game():
        number = input("How many people are playing? :")
        n_players = int(number)
        all_names = []
        for each in range(0,n_players):
            name = input("Name player? :")
            all_names.append(name)
     
        player_list= []
        for each in all_names:
            player = Player(each)
            player_list.append(player)
        
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()
        deck.distribute(n_players,player_list)
        
        playing_field = Board()
        
        while len(player.hand) >0:          
            for each in player_list:
                each.play()                
            playing_field.turn_count+=1
            print("Turn count is:", playing_field.turn_count)

