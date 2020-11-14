from random import *
import collections as cl

Card = cl.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    """
        creer un deck
    """
    ranks = [str(n) for n in range(2,11)] + list('JQRA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self,positions):
        return self._cards[positions]
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)
    deck = FrenchDeck()
    print("1-: ","la taille du paquet est de:",len(deck),"cartes")
    print("2-: ","liste des cartes du deck:")
    x = 0
    while x < 52:
        #if x == 52:
            #break
        for card in sorted(deck,key=spades_high): 
            x += 1 
            print("3-: ","\t",x,card)
    print("4-: ",choice(deck))
