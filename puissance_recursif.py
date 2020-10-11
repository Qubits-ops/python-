def puissance(x:int,y:int)-> int:
    """
        fonction recursif pour calculer une puissance
        prend un nombre entier et la puissance par laquelle on veux multiplier
        retourne x puissance y
        
        >>>puissance(10,5)
        100000
    """
    if y == 1:
        return x#cas de base
    else:
        return x*puissance(x,y-1)#cas de propagation
print(puissance(10,5))
