# import snss
import sys
print('sys.path = ', sys.path)
sys.path.append(r"F:\Python\Script\Chromagnon-SNSS")
print('sys.path = ', sys.path)
from chromagnon import *
# sys.path.append(r"F:\Python\Script\yandex-music\yandex-music-api")
# from yandex_music import *
# import chromagnon
import chromagnon.SNSSParse
import chromagnon.sessionParse


if __name__ == '__main__':
    path = r'F:\Python\Script\Project_SNSS\paths.lst'
#    paths = open(path, mode='r', encoding='utf-8')
    paths = open(path, mode='r')
    for path in paths:
        path.strip('\r\n')
        print('paths = ', paths, ' path = ', path)
#    print(snss())
#    print('sys.modules = ', sys.modules)
        snss = chromagnon.SNSSParse.parse(path)
#        print('snss = ', snss)
        sessionCommand = chromagnon.sessionParse.parse(snss)
#        print('sessionCommand = ', sessionCommand)
        print('type(sessionCommand) = ', type(sessionCommand), len(sessionCommand))
        for command in sessionCommand:
            print(command)
        print('sessionCommand[0] = ', sessionCommand[0])
        print('sessionCommand[1] = ', sessionCommand[1])
    print()
