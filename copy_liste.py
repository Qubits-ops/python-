def copy(a:list)->list:
    i = [];
    for x in a:
        i.append(x)
    return i
li = [1,2,3,4,5]
copi = copy(li)
li.clear()
print(li)
print(copi)
