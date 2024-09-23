def function(dc,dc1):
        summa = 0
        dc1 = {}
        for x in dc:
                k = dc[x]
                q = sum(k) // len(k)
                dc1.update({x: q})
        return dc1
p = 1
dc = {}
dc1 = {}
while p:
        n = list(map(int,input("Ballar >>> ").split()))
        k = str(input("Ismi >>> "))
        dc.update({k : n})
        dc1 = function(dc,dc1)
        p = int(input(" 1 - Davom etirish, 0 -Toxtatish"))
import os
os.system("clear")
print(dc1)
