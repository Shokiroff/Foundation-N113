dict = {"Munisa": [100,98,45,87,88], "Aziza": [55,87,90,99,46,89], "Komola": [45,98,56,88,45]}

result_dict = {}

for x in dict:
    summ = sum(dict[x])//len(dict[x])
    result_dict[x] = summ

print(result_dict)
