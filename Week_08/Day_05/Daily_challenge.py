import random


# Exercise 1 - Quizz

# 1) A Class is like an object constructor, or a "blueprint" for creating objects.
# 2) An instance is a specific realization of any object
# 3) Encapsulation refers to the bundling of data with the methods that operate on that data, or the restricting of direct access to some of an object's components
# 4) Abstraction is the process of filtering out - essentially ignoring - the characteristics of problems that are not needed in order to concentrate on those that are needed
# 5) Inheritance is a mechanism of acquiring the features and behaviors of a class by another class
# 6) Multiple inheritance enables a derived class to inherit members from more than one parent.
# 7) Polymorphism is a feature of object-oriented programming languages that allows a specific routine to use variables of different types at different times.
# 8) Method Resolution Order(MRO) it denotes the way a programming language resolves a method or attribute

# Exercise 2

class Card:
    suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
    value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cards1 = [x + " Hearts" for x in value]
    cards2 = [x + " Diamonds" for x in value]
    cards3 = [x + " Clubs" for x in value]
    cards4 = [x + " Spades" for x in value]
    cards = cards1 + cards2 + cards3 + cards4


class Deck(Card):
    def shuffle(self):
        random.shuffle(Card.cards)
        for i in Card.cards:
            print(i, end=" ")
        print("\n")

    def deal(self):
        deal_card = random.choice(Card.cards)
        print(f"The card is: {deal_card}")
        Card.cards.remove(deal_card)
        for i in Card.cards:
            print(i, end=" ")


cards = Card()
cards2 = Deck()
print("Showing original list of cards:")
print(cards.cards)
print("Showing cards after shuffle:")
cards2.shuffle()
print("Showing deal card and list after deal card removed")
cards2.deal()
