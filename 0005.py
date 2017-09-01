# _*_ coding: utf-8 _*_

#������
#����һ��Ŀ¼��װ�˺ܶ���Ƭ�������ǵĳߴ��ɶ������� iPhone5 �ֱ��ʵĴ�С

from PIL import Image
import os

fpath = 'source/0005/pics'
rpath = 'source/0005/results'

if not os.path.isdir(rpath):  #here os.path.exists(result_path):
    os.mkdir(rpath)
for picName in os.listdir(fpath):
    #png ��ʽ��ͼƬҲ���ɴ�
    picPath = os.path.join(fpath, picName)  
    #join the fpaht and the name of the pic as a new path, as is shown picPath.
    print(picPath)
    with Image.open(picPath) as im:
        w, h = im.size
        n = w / 1366 if (w / 1366) >= (h / 640) else h / 640
        #˭�ı�����ѡ��˭, �������Եõ����õı���
        im.thumbnail((w / n, h / n))
        im.save(rpath + '/finish_' + picName, 'jpeg')
        
        #����Ҳ����rpath, ��ô���ɵ�ͼ���ڳ������ڵ��ļ��г���
        #'/finish_' û��/���ŵĻ�����ô���е�ͼƬ���������0005�ļ���֮�ڣ�results�Լ�
        #finish �����������ֵ�һ���֡�
        #����thumbnail()��Ҫ���ֿ�߱ȣ�����(200,200)���������
        #ԭ��(800,450)�����(200,112)��ԭ��(450,800)�����(112,200)��
