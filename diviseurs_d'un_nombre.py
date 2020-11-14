def diviseur_nb(n:int)->list:
    assert n > 1 , 'l\'entier dois etre superieur a 1'
    
    ma_liste = []
    b = n/2
    i = 2
    cpt1 = 0
    while i <= b:
        if n%i == 0:
            cpt1+=1
            ma_liste.append(i)
        i+=1
    #del ma_liste[-1]
    if len(ma_liste) == 0:
        return " votre nombre est premier"
    return ma_liste
        
        
print(diviseur_nb(12))
