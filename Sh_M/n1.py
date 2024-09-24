def fun(arr, sz):
    re = []
    
    for i in range(0, len(arr), sz):
        re.append(arr[i:i + sz])

    return re

ber = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
sz = int(input("Son: "))

re = fun(ber, sz)
print(re)