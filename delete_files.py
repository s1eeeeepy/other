import os


p = r"D:\\coding\\trash"
for file in os.listdir(p):
    if "Folder" in file:
        os.rmdir(os.path.join(p, file))
        print(f"{file} --- removed")
        print("==============================================================")
