def hanoi(n,A=1,B=2,C=3):
    """
        programme recursif sur le jeux tours de hanoi
    """
    if n > 0:
        hanoi(n-1,A,C,B)
        print("on deplace ",A," sur ",C)
        hanoi(n-1,B,A,C)
print(hanoi(3))
