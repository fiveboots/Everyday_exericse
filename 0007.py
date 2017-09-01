# _*_ coding:utf-8 _*_
#有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来
import re
import os

def count_numbers(load_path):
    if not os.path.isdir(load_path):
        print('Sorry, we cannot fint the file, please check the file-path again.')
    tplt = "{:^10}\t{:^10}\t{:^10}\t{:^10}"
    #print('filename\tall-lines\tspace-lines\texp-lines')
    print(tplt.format('filename', 'all-lines', 'space-lines', 'exp-lines'))
    filelist = os.listdir(load_path)
    exp_re = re.compile('^#.*')
    for fileName in filelist:
        fpath = os.path.join(load_path, fileName)
        if os.path.isfile(fpath) and os.path.splitext(fpath)[1] == '.py':
            with open(fpath) as f:
                all_lines = 0
                space_lines = 0
                exp_lines = 0
                for line in f.readlines():
                    all_lines += 1
                    if line.strip() == '':
                        space_lines += 1
                        #continue #I don't know what will happen if we dont use the continue.
                    check_exp = exp_re.findall(line.strip())
                    # if we don't use the line.strip() then this line will be ignored.
                    # because it is started with blanks.
                    if check_exp:
                        #print(check_exp)
                        exp_lines += 1
            print(tplt.format(fileName, all_lines, space_lines, exp_lines))

if __name__ == '__main__':
    count_numbers('.')
