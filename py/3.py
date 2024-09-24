def list_to_dict(myList):
    myDct = {}
    for num in myList:
        if num in myDct:
            myDct[num] += 1
        else:
            myDct[num] = 1
    return myDct

myList = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
myDct = list_to_dict(myList)
print(myDct)
