def length(a:str)->int:
    """
        reproduction de la fonction len
    """
    x = 0
    while x != len(a):
        x+=1
    return x
print(length("bonjour mec"))
