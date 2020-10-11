def factorielle(n:int)->int:
    """
        fonction recursive factorielle
    """
    if n == 1:
        return 1
    else:
        return n * factorielle(n-1)
print(factorielle(10))
