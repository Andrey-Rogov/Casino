import collections
from random import choice
Card = collections.namedtuple('Card', ['rank', 'suit'])


class Deck:
    ranks = [str(n) for n in range(6, 11)] + ["J", "Q", "K", "A"]
    suits = ["hearts", "spades", "diamonds", "clubs"]

    def __init__(self):
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, item):
        return self.cards[item]


frenchdeck = Deck()
money = 100


def casino(pred):
    thing = choice(frenchdeck)
    if pred == 'black' and (thing.suit == 'spades' or thing.suit == 'clubs'):
        print("Yes! The card is:", *thing)
        return True
    elif pred == 'red' and (thing.suit == 'diamonds' or thing.suit == 'hearts'):
        print("Yes! The card is:", *thing)
        return True
    else:
        print("Oh no.. The card is:", *thing)
        return False


print("You can predict if the random card will be: black or red")
print("The input should look like 'black 100'")
while True:
    print("You have", money)
    print("-----------------")
    if money <= 0:
        print("You don't have enough money!\nYou lose!")
        break
    elif money >= 300:
        print("You tripled your money!\nYou won!")
        break
    inp = input("Color of card and bet: ").split()
    deal, bet = inp[0], int(inp[1])
    if bet > money:
        print("You can't afford this bet")
        print()
        continue
    if casino(deal):
        money += bet
    else:
        money -= bet
    print()
