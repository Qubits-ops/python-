def copy_dico(a:dict)->dict:
    dico1 = {}
    for x in a.keys():
        for valeur in a.values():
            dico1[x] = valeur
    return dico1
 di = {"batman":"joker"}
 print(di)
 x = copy_dico(di)
 di.clear()
 print(di)
 print(x)
