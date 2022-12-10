#!/usr/bin/env python
# coding: utf-8

from PIL import Image, ImageDraw, ImageFont


def has_transparency(img):
    if img.info.get("transparency", None) is not None:
        return True
    if img.mode == "P":
        transparent = img.info.get("transparency", -1)
        for _, index in img.getcolors():
            if index == transparent:
                return True
    elif img.mode == "RGBA":
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            return True

    return False
        

if __name__ == "__main__":
    pic1_16_9 = Image.open('PIC1.png')
    pic1_4_3 = Image.open('PIC1.png').crop((130,0,1600,1080))
    pic0 = Image.open('PIC0.png')
    icon0 = Image.open('ICON0.png')

    # 16:9
    if has_transparency(icon0):
        Image.Image.paste(pic1_16_9, icon0, box=(475, 400), mask=icon0)
    else:
        Image.Image.paste(pic1_16_9, icon0, box=(475, 400))
    if has_transparency(pic0):
        Image.Image.paste(pic1_16_9, pic0, box=(750, 420), mask=pic0)
    else:
        Image.Image.paste(pic1_16_9, pic0, box=(750, 420))
    pic1_16_9.show()

    # 4:3
    pic0 = pic0.resize((700,400))
    if has_transparency(icon0):
        Image.Image.paste(pic1_4_3, icon0, box=(345, 400), mask=icon0)
    else:
        Image.Image.paste(pic1_4_3, icon0, box=(345, 400))
    if has_transparency(pic0):
        Image.Image.paste(pic1_4_3, pic0, box=(630, 490), mask=pic0)
    else:
        Image.Image.paste(pic1_4_3, pic0, box=(630, 490))
    pic1_4_3.show()
    
    
