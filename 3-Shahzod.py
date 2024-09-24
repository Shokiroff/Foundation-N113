def function(ls):
    dc = {}
    k = ls[0]
    for x in ls:
        if k != x:
            dc.update({k : ls.count(k)})
            k = x
    return dc
ls = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
dc = function(ls)
print(dc)