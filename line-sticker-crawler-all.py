import requests as RS
from bs4 import BeautifulSoup as BS
import os
import shutil
from time import sleep
import random
import settings

web_base1 = "https://store.line.me/stickershop/product/"
web_base2 = "/zh-Hant"
select = "span.mdCMN09Image"
sticker_id_start = int(settings.start)
sticker_id_end = int(settings.end)
file_type = ".png"
file_store = settings.file_store

for sticker_id_i in range(sticker_id_start, sticker_id_end) :
    web = web_base1 + str(sticker_id_i) + web_base2
    print("Now is " + web)
    try :
        web = RS.get(web, timeout=1)
    except Exception:
        print("The page may timeout")
        continue
    if web.status_code == 200:
        soup = BS(web.text, "html.parser")
        stickers = soup.select(select)
        dire = file_store + str(sticker_id_i) + "/"
        if len(stickers) != 0 and not os.path.exists(dire):
            os.makedirs(dire, exist_ok=True)
            for sticker in stickers :
                i = sticker["data-sticker-id"]
                href = sticker["style"].split("url(")[-1].split(");")[0]
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

    wait = random.randint(1, 10)
    print("waiting " + str(wait) + " seconds...")
    sleep(wait)

print("下載完成")


