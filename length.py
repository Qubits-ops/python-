def length(a:str or list or dict or tuple)->int:
        c = 0
        for i in a:
            c+=1
        return c        

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    print(length("bonjour, maitre"))

