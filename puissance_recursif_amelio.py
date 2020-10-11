def puissance(x,y):
    if y == 1:
        return x
    if y % 2 == 0:
        return puissance(x*x,y//2)
    else:
        return puissance(x*x,(y-1)//2)
print(puissance(10,5))
