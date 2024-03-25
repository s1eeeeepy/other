from random import randrange


count = 0
while count < 50:
    with open("division_10000.txt", "a") as file:
        x = randrange(10000, 100000)
        y = randrange(3, 10)
        if x % y == 0:
            file.writelines(f"{x} / {y} = {int(x/y)}\n")
            count += 1
        else:
            continue
