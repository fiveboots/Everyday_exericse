# _*_ coding: utf-8 _*_

#第五题
#你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小

from PIL import Image
import os

fpath = 'source/0005/pics'
rpath = 'source/0005/results'

if not os.path.isdir(rpath):  #here os.path.exists(result_path):
    os.mkdir(rpath)
for picName in os.listdir(fpath):
    #png 格式的图片也都可打开
    picPath = os.path.join(fpath, picName)  
    #join the fpaht and the name of the pic as a new path, as is shown picPath.
    print(picPath)
    with Image.open(picPath) as im:
        w, h = im.size
        n = w / 1366 if (w / 1366) >= (h / 640) else h / 640
        #谁的倍数大，选择谁, 这样可以得到更好的倍数
        im.thumbnail((w / n, h / n))
        im.save(rpath + '/finish_' + picName, 'jpeg')
        
        #如果我不添加rpath, 那么生成的图会在程序所在的文件夹出现
        #'/finish_' 没有/符号的话，那么所有的图片将会出现在0005文件夹之内，results以及
        #finish 都会变成新名字的一部分。
        #方法thumbnail()需要保持宽高比，对于(200,200)的输入参数
        #原来(800,450)，变后(200,112)；原来(450,800)，变后(112,200)；
