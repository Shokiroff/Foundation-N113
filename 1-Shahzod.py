def function(ls,n):
        i = 0
        j = 0
        ls1 = list()
        ls2 = list()
        while len(ls) > j:
                if i != n:
                        ls1.insert(len(ls1),ls[j])
                        i += 1
                else:
                        j -= 1
                        i = 0
                        ls2.append(ls1)
                        ls1 = list()
                j += 1
        ls2.append(ls1)
        return ls2
n = int(input("N >>> "))
ls = ["A","B","C","D","E","F","G","L","Q","U"]
k = function(ls,n)
print(k)