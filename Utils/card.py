""" 
In this file we define what a card exactly is. A deck has 52 cards,
which consists of 4 symbols each of which have 13 values. The symbols are 
hearts and diamonds which are red, and spades and clubs which are black.
"""


"""
In the Symbol class we create a blueprint for these cards and determine their
symbols(aka icons).
"""

class Symbol:
    color = ("red","black")
    icon = ("♥","♦", "♣", "♠")
    def __init__(self, color, icon):
        self.color = color
        self.icon = icon

"""
The class Card is a child from Symbol, inheriting the icon and color but
adding a value to the mix. It's these values that determine a card's worth 
throughout a variation of games.
"""

class Card(Symbol):
    value = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
    def __init__(self, color, icon, value):
        Symbol.__init__(color, icon)
        self.value = value

    def __str__(self):
        return f"You played the {self.value} of {self.icon}, which is {self.color}"
