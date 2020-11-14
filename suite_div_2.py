def suite_div_2(n:int)->list and int:
    ma_liste = []
    ma_liste2 = []
    while n > 1 :
        n  = n // 2
        ma_liste.append(round(n,1))
    print(ma_liste)
    return len(ma_liste)

print(suite_div_2(10))
