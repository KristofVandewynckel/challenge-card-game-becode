class Symbol:
    def __init__(self):
        color = ["red","black"]
        icon = ["hearts","diamonds","clubs","spades"]
        self.color = color
        self.icon = icon
class Card(Symbol):
    def __init__(self):
        Symbol.__init__(self)
        value = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.value = value
        print(value)
#    def __str__(self):
#       return f"You played the {self.value} of {self.icon}, which is {self.color}"
Card()