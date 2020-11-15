def copy(a:list or str or int or dict)->list or str or int or dict:
    if type(a) == list:
        i = [];
        for x in a:
            i.append(x)
        return i
    elif type(a) == dict:
        dico1 = {}
        for x in a.keys():
            for valeur in a.values():
                dico1[x] = valeur
        return dico1
    elif type(a) == int:
        nb = a
        return nb
    elif type(a) == str:
        strt = a
        return strt
li = [1,2,3,4,5]
copi = copy(li)
li.clear()
print(li)
print(copi)
