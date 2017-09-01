# _*_ coding: utf-8 _*_

# 第 0010 题：使用 Python 生成类似于下图中的字母验证码图片
# 我们在这个基础上稍微修改了下，温习了一下os,以及将一定数量的二维码保存到固定路径
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string
import os

def rdmChar():
    return chr(random.randint(65, 90))

def rdmColor1():
    a = random.randint(64, 255)
    return (a, random.randint(64, 255), random.randint(64, 255))

def rdmColor2():
    c = random.randint(32, 127)
    return (random.randint(32, 127), random.randint(32, 127), c)

def create_pics(number, root):
    if not os.path.isdir(root):
        os.mkdir(root)
    for a in range(number):
        width = 60 * 4
        height = 60
        image = Image.new('RGB', (width, height), (255, 255, 255))
        font = ImageFont.truetype('C:/Windows/Fonts/ARIALUNI.TTF', size=36)

        #we will do something on the pic, 
        #so we creat a draw model will carry out on it.
        draw = ImageDraw.Draw(image)
        # fill every pixel with a random color.
        for x in range(width):
            for y in range(height):
                draw.point((x, y), fill=rdmColor1())

        for t in range(4):
            draw.text((60 * t + 10, 10), rdmChar(), font=font, fill=rdmColor2())

        image = image.filter(ImageFilter.BLUR)
        
        image_name = ''
        for i in range(6):
            image_name += random.choice(string.digits)
        image.save(root + image_name + '_code.jpg', 'jpeg')

if __name__ == '__main__':
    root = 'source/0010/'
    create_pics(20, root)
