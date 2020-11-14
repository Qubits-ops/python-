def length(a:str or list or dict or tuple)->int:
    """
        reproduction de la fonction len
    """
    x = 0
    while x != len(a):
        x+=1
    return x

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    print(length("bonjour, maitre"))

