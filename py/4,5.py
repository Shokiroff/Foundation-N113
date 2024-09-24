data = [
    {"model": "RDX", "year": 2009},
    {"model": "LS", "year": 2000},
    {"model": "GLK-Class", "year": 2010},
    {"model": "Express 1500", "year": 2005},
    {"model": "LR2", "year": 2008},
    {"model": "XF", "year": 2012},
    {"model": "MR2", "year": 2005},
    {"model": "Malibu", "year": 2007},
    {"model": "M-Class", "year": 2010},
    {"model": "Routan", "year": 2011}
]

sort = sorted(data, key = lambda x: x['year'])

for x in sort:
    print(f"Model: {x['model']}, Year: {x['year']}")

with open("malibu.txt", "wt") as file:
    for x in sort:
        file.write(f"Model: {x['model']}, Year: {x['year']}\n")
