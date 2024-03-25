import os
import shutil
import random


hip_hop = "D:\LDS\Music\src\hip_hop"
shuffle = "D:\LDS\Music\src\shuffle"
dst = "D:\LDS\Music\msc"

hop = "Moving Hip Hop"
sfl = "Moving Shuffle"


def get_songs(src, dst):
    tracks = []
    folder = src.split("\\")[-1]
    while len(tracks) < 10:
        item = random.choice(os.listdir(src))
        if item not in tracks:
            tracks.append(item)
    for i in tracks:
        name = f"{src}\{i}"
        dest = f"{dst}\{folder}\{i}"
        shutil.move(
            name,
            dest,
        )
        print(f"{i} added!")


if __name__ == "__main__":
    print(f"{hop:-^74}")
    get_songs(hip_hop, dst)
    print(f"{sfl:-^74}")
    get_songs(shuffle, dst)
