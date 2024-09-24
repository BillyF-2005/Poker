import cardShuffler as cs

numOfPlayers = 10
players = []
playedCards = []
sharedCards = []

class person():
    def __init__(self,playedCards,sharedCards):
        self.hand = [cs.shuffle(),cs.shuffle()]
        while (self.hand[0] in(playedCards)) or (self.hand[0] == self.hand[1]):
            self.hand[0] = cs.shuffle()
        while self.hand[1] in(playedCards):
            self.hand[1] = cs.shuffle()
        self.myCards = sharedCards
        self.myCards.append(self.hand)
        

for i in range(numOfPlayers):
    players.append([])
    players[i] = (person(playedCards,sharedCards))
    playedCards.append(players[i].hand[0])
    playedCards.append(players[i].hand[1])
    
