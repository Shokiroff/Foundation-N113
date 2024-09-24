lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'L', 'Q', 'U']

def split_list(lst, n):
    result = [lst[i:i + n] for i in range(0, len(lst), n)]
    return result


n = int(input("n ni kiriting"))
out = split_list(lst, n)
print("Natija:", out)
