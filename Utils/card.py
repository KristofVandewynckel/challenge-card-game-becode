class Symbol:
    color = ("red","black")
    icon = ("♥","♦", "♣", "♠")
    def __init__(self, color, icon):
        self.color = color
        self.icon = icon

class Card(Symbol):
    value = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
    def __init__(self, color, icon, value):
        Symbol.__init__(color, icon)
        self.value = value

    def __str__(self):
        return f"You played the {self.value} of {self.icon}, which is {self.color}"














"""class Symbol:   
    def __init__(self,color, icon):
        color = ["red","black"]
        icon = ["hearts","diamonds","clubs","spades"]
        self.color = color
        self.icon = icon
class Card(Symbol):
    def __init__(self,color, icon, value):
        value = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
        Symbol.__init__(self, color, icon)
        self.value = value
    def __str__(self):
       print( f"You played the {self.value} of {self.icon}, which is {self.color}")

played_card = Card("red","hearts","5")
print(played_card)"""


"""class Symbol:
    color = ["red","black"]
    icons = ["hearts","diamonds","clubs","spades"]
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self, icon, color):
        self.icon = icon
        self.color = color
class Card(Symbol):
    def __init__(self, icon, color, value):
        Symbol.__init__(self, icon, color)
        self.value = value
        return f"You've played the {self.value} of {self.icon}"

Card("hearts","red","2")"""