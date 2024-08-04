from operator import index
import random



def shuffle(i):
    suits = ['club', 'diamond', 'heart', 'spade']
    values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    faces = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

    cardSuit = random.choice(suits)
    cardValue = random.choice(values)
    cardFace = faces[values.index(cardValue)]
    card = [cardSuit,cardFace,cardValue]
    return card[i]
    
