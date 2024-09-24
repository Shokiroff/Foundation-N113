ls = input("List elementlarini kiriting : ")
numbers = [int(num) for num in ls.split()]
dc = {}
for x in numbers:
    if x in dc:
        dc[x] += 1
    else:
        dc[x] = 1
print("", dc)
