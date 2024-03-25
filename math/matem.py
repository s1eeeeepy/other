import random


with open("mat.txt", "w") as f:
    for _ in range(100):
        a = random.randint(10, 1000)
        b = random.randint(2, 10)
        f.write(f"{a} * {b} = {a * b}\n")
