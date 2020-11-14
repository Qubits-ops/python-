def pi():
    pi = 3.141592663589793138462645118
    return pi
def cone_droit(r:int,h:int)->int:
    volume = pi() * r**2 / 3 * h
    volume1 = round(volume,1)
    return volume1
print(cone_droit(2,10),"cm3")
    
    
