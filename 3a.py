myList = [1, 1, 2, 3, 3, 4, 2, 3, 4, 1, 2, 3]

def sanash(lst):
    dct = {}
    for i in lst:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    return dct

myDict = sanash(myList)
print(myDict)
