myList = [1, 1, 2, 3, 4, 3, 2, 3, 4, 2, 1, 2, 3]

def count_elements(lst):
    element_count = {}
    for item in lst:
        if item in element_count:
            element_count[item] += 1
        else:
            element_count[item] = 1
    return element_count
myDict = count_elements(myList)
print("Natija:", myDict)
