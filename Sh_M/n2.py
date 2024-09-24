def fn(mls):
    qwe = {}
    for x in mls:
        if x in qwe:
            qwe[x] += 1
        else:
            qwe[x] = 1
    return qwe

mls = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
qwe = fn(mls)
print(qwe)