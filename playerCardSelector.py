from cardShuffler import shuffle
from operator import index
import operator

#numOfPlayers = int(input('how many people are playing? '))
balance1 = ('what is player 1s balance? ')
balance2 = ('what is player 2s balance? ')

playedCards = []

class Person():
    def __init__(self, card1, card2, balance):
        self.card1 = card1
        self.card2 = card2
        self.balance = balance
#    def cardCheck(self, card1, card2):
#        self.card1 = card1
#        self.card2 = card2
#        print(card1)
#        print(card2)
    
def cardCheck(c1,c2,playedCards):
        while playedCards.count(c1) > 0:
            c1 = shuffle()
            print('reshuffling card')
        if playedCards.count(c1) == 0:
            playedCards.append(c1)
            print('card 1 ok')
        while playedCards.count(c2) > 0:
            c2 = shuffle()
            print('reshuffling card')
        if playedCards.count(c2) == 0:
            playedCards.append(c2)
            print('card 2 ok')
        return c1,c2,playedCards



#p1Balance = float(input('what is your balance '))

p1 = Person(shuffle(),shuffle(),balance1)
p1FinalCards = cardCheck(p1.card1,p1.card2,playedCards)
p1.card1 = p1FinalCards[0]
p1.card2 = p1FinalCards[1]
#print(playedCards)
#playedCards = playedCards + p1FinalCards[2] 
#playedCards = playedCards + p1.playedCards
p2 = Person(shuffle(),shuffle(),balance2)
p2FinalCards = cardCheck(p2.card1,p2.card2,playedCards)
p2.card1 = p2FinalCards[0]
p2.card2 = p2FinalCards[1]
#playedCards = playedCards + cardCheck(p2.card1,p2.card2,playedCards)[2] 
#playedCards = playedCards + p2.playedCards
#while p1.card1 == (p2.card1 or p2.card2) or p1.card2 == (p2.card1 or p2.card2):
#    p2 = person()
"""
print(p1.card1,p1.card2)
print(p2.card1,p2.card2)

print(playedCards)"""
"""
def playerCardSelect(person):
    p1 = person(shuffle(),shuffle(),balance1)
    p1FinalCards = cardCheck(p1.card1,p1.card2,playedCards)
    p1.card1 = p1FinalCards[0]
    p1.card2 = p1FinalCards[1]
    p2 = person(shuffle(),shuffle(),balance2)
    p2FinalCards = cardCheck(p2.card1,p2.card2,playedCards)
    p2.card1 = p2FinalCards[0]
    p2.card2 = p2FinalCards[1]
    people = p1,p2
    return people

"""



