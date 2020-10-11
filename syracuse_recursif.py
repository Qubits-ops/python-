def syracuse(n:int)->int:
    """
        fonction recursive de syracuse
        prend un entier positif en parametre
        retourne 1
        
        >>>syracuse(19)
        1
    """
    if n == 1:
        return 1#cas de base
    elif n%2 == 0:
        return syracuse(n//2)#cas de propagation
    else:
        return syracuse(3*n+1)#cas de propagation
print(syracuse(19))
