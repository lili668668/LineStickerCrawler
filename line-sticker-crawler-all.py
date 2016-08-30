import requests as RS
import os
import shutil
from time import sleep
import random

base1 = "https://sdl-stickershop.line.naver.jp/products/0/0/1/"
base2 = "/android/stickers/"
sticker_id_start = 3006
sticker_id_end = 3010
file_type = ".png"
file_store = "/home/ballfish/VM/crawler_line_sticker/stickers/"
start = 695383

i = start

for sticker_id_i in range(sticker_id_start, sticker_id_end) :
    dire = file_store + str(sticker_id_i) + "/"
    os.makedirs(dire, exist_ok=True)
    base = base1 + str(sticker_id_i) + base2
    href = base + str(i) + file_type
    pic = RS.get(href, stream=True)
    while pic.status_code == 200:
        path = dire + str(i) + file_type
        picture = open(path, "wb")
        shutil.copyfileobj(pic.raw, picture)
        print(str(i) + " loading...")
        picture.close()

        i = i + 1
        href = base + str(i) + file_type
        pic = RS.get(href, stream=True)

    wait = random.randint(1, 5)
    print("waiting " + str(wait) + " seconds...")
    sleep(wait)

print("下載完成")


