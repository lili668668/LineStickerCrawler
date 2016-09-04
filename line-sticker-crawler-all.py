import requests as RS
from bs4 import BeautifulSoup as BS
import os
import shutil
from time import sleep
import random

base1 = "https://sdl-stickershop.line.naver.jp/products/0/0/1/"
base2 = "/android/stickers/"
web_base1 = "https://store.line.me/stickershop/product/"
web_base2 = "/zh-Hant"
select = "span.mdCMN09Image"
sticker_id_start = 3105
sticker_id_end = 3200
file_type = ".png"
file_store = "/home/ballfish/VM/crawler_line_sticker/stickers/"

for sticker_id_i in range(sticker_id_start, sticker_id_end) :
    web = web_base1 + str(sticker_id_i) + web_base2
    print("Now is " + web)
    web = RS.get(web)
    if web.status_code == 200:
        soup = BS(web.text, "html.parser")
        stickers = soup.select(select)
        if len(stickers) != 0 :
            dire = file_store + str(sticker_id_i) + "/"
            os.makedirs(dire, exist_ok=True)
            base = base1 + str(sticker_id_i) + base2
            for sticker in stickers :
                i = sticker["data-sticker-id"]
                href = base + str(i) + file_type
                pic = RS.get(href, stream=True)
                if pic.status_code == 200:
                    path = dire + str(i) + file_type
                    picture = open(path, "wb")
                    shutil.copyfileobj(pic.raw, picture)
                    print(str(i) + " loading...")
                    picture.close()
                else :
                    print("Sticker load fail")
        else :
            print(str(sticker_id_i) + " there is no sticker")
    else :
        print("The page may not found")

    wait = random.randint(1, 5)
    print("waiting " + str(wait) + " seconds...")
    sleep(wait)

print("下載完成")


