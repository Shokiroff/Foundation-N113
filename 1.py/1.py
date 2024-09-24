def split_list(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

n = int(input("Bo'lak uzunligini kiriting: "))
lst = ["A", "B", "C", "D", "E", "F", "G", "L", "Q", "U"]
lst1 = split_list(lst, n)
print(lst1)
