def pgcd(a:int,b:int)->int:
    """
        fonction recursive de pgcd(PLUS GRAND DIVISEUR COMMUN DE DEUX NOMBRES)
        
        >>>pgcd(24,18)
        6
    """
    if b == 0:
        return a
    else:
        return pgcd(b,a%b)
print(pgcd(24,18))
