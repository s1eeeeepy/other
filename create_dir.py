import os


p = "/d/coding/trash"
count = 0
for _ in range(10):
    count += 1
    os.mkdir(f"Folder {count}")
