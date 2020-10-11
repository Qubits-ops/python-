def binaire(n:int)->list:
    """
        conversion binaire recursive
        prend un entier positif en parametre
        affiche la conversion binaire du nombre decimal entrer
        
        >>>binaire(10)
        [1,0,1,0]
    """
    assert type(n) != str , 'cela doit etre un nombre'
    if n == 0:
        return []#cas de base
    else:
        quotient = n//2
        reste = n%2
        return binaire(quotient) + [reste]#cas de propagation
print(binaire(3))
