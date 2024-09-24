lst = ["A", "B", "C", "D", "E", "F", "G", "L", "Q", "U"]

inp1 = int(input("Bo'lish kerak bo'lgan sonni kiriting: "))

def bolib_ber(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

output = bolib_ber(lst, inp1)
print(output)
