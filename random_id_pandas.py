import pandas as pd
import random as rd
import time

year = int(input("ID 63 or 64 or 65 << ")) 

if year == 65:
    file = "multi65.txt"
elif year == 64:
    file = "multi64.txt"
elif year == 63:
    file = "multi63.txt"

x = pd.read_csv(file, header=None)
x = x.values.tolist()

rd.shuffle(x)
x_new = rd.sample(x, len(x))

print(f"ลำดับ \t รหัส \t ชื่อ ".expandtabs(5))

for n, i in enumerate(x, 1):
    time.sleep(.5)
    print(f"{n} \t {i[0]} {i[1]} ".expandtabs(4))
