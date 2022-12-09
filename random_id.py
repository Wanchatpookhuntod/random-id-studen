import random
import time

year = int(input("ID 63 or 64 or 65 << ")) 

if year == 65:
    file = "multi65.txt"
elif year == 64:
    file = "multi64.txt"
elif year == 63:
    file = "multi63.txt"

tables = []

with open(file, "r") as f:
    data = f.readlines()
    for i in data:
        
        tables.append(i.splitlines())

random.shuffle(tables)
tables = random.sample(tables, len(tables))

for n, i in enumerate(tables, 1):
    i = i[0].split(",")
    time.sleep(.4)
    print(f"{n} \t {i[0]} {i[1]} ".expandtabs(4))
