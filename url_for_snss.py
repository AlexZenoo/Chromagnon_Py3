# -*- coding: utf-8 -*-
# import snss
import sys

import chromagnon # вот где ошибка! мало импортировать имя пакета!

print('sys.path = ', sys.path)
# sys.path.append(r"F:\Python\Script\Chromagnon-SNSS")
sys.path.append(r"F:\Python\Script\Chromagnon_Py3")
sys.path.append(r"F:\Python\Script")
print('sys.path = ', sys.path)
print('import 0!')
# from chromagnon import *
# sys.path.append(r"F:\Python\Script\yandex-music\yandex-music-api")
# from yandex_music import *
# import chromagnon
# from Books_Lib import print_to_file
# import Books_lib.print_to_file
# from Books_Lib import print_to_file
# import Books_Lib.print_to_file
# from chromagnon import __init__ as root
print('import 1')
import chromagnon.SNSSParse
print('import 2')
import chromagnon.sessionParse
print('import 3')

def log_to_file(path):
    file_path = open(path, mode='w')
    print('file_log = ', file_path)
    sys.stderr = file_path
    sys.stdout = file_path
    return True

def log_orig():
    sys.stderr = sys.__stderr__
    sys.stdout = sys.__stdout__


if __name__ == '__main__':
#    output_new = list()
#    command_list = list()
#    output_new = root.output_new
    output_new = chromagnon.output_new
#    command_list = root.command_list
    command_list = chromagnon.command_list
    print('dir chromagnon = ', dir(chromagnon))
    print('dir chromagnon.sessionParse = ', dir(chromagnon.sessionParse))
    print('dir chromagnon.SNSSParse = ', dir(chromagnon.SNSSParse))
    log_to_file(r'F:\Python\Books_Lib\Base_YAML\temp_print_SNSS.txt')
    path = r'F:\Python\Script\Project_SNSS\paths.lst'
#    paths = open(path, mode='r', encoding='utf-8')
    paths = open(path, mode='r')
    for path in paths:
#        path.strip(r'\r\n')
#        path.strip(r'\n')
#        path.rstrip(r'\r', r'\n')
#        path.rstrip(r'\n')
#        path.strip() # rrrrrr!
        path = path.strip()
        print('paths = ', paths, ' path = ', path)
#    print(snss())
#    print('sys.modules = ', sys.modules)
#        snss = chromagnon.SNSSParse.parse(path)
        snss, snss_new = chromagnon.SNSSParse.parse(path)
#        print('snss = ', snss)
#        print('snss = ', snss, ' snss_new = ', snss_new)
        print('snss_new = ', snss_new)
#        print('type(snss) = ', type(snss), ' type(snss_new) = ', type(snss_new))
        print('output_new = ', output_new)
        sessionCommand = chromagnon.sessionParse.parse(snss)
#        print('sessionCommand = ', sessionCommand)
        print('type(sessionCommand) = ', type(sessionCommand), len(sessionCommand))
        for command in sessionCommand:
            print(command)
#        print('sessionCommand[0] = ', sessionCommand[0])
#        print('sessionCommand[1] = ', sessionCommand[1])
        print('command_list = ', command_list)
    print('END!')
    log_orig()