from random import *
import collections

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    """
        creer un deck
    """
    ranks = [str(n) for n in range(2,11)] + list('JQRA')
    suits = 'spades diamons clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self,positions):
        return self._cards[positions]
deck = FrenchDeck()
print("1-: ","la taille du paquet est de:",len(deck),"cartes")
print("2-: ","liste des cartes du deck:")
x = 0
while x < 52:
    #if x == 52:
        #break
    for d in deck:
        x += 1 
        print("3-: ","\t",x,d)
print("4-: ",choice(deck))
