# -*- coding: utf-8 -*-

def file_write(file_name):
    f = open(file_name, 'w')
    print('请输入内容【单独输入\':q\'保存退出】：')

    while True:
        file_content = input()
        if file_content != ':q':
            f.write('%s\n' % file_content)
        else:
            break

    f.close()

file_name = input('请输入文件名：')
file_write(file_name)
