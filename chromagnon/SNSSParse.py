#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012, Jean-Rémy Bancel <jean-remy.bancel@telecom-paristech.org>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the Chromagon Project nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Jean-Rémy Bancel BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
Reverse engineered from chrome/browser/sessions/*
"""

import os
import struct

import types

SNSS_MAGIC = 0x53534E53
iterr = 0

def parse(path):
    """
    Parses SNSS files and returns a list of SNSS command objects
    """
    output = []
    output_new = []

    f = open(path, 'rb')
    print('f = ', f)
    f.seek(0, os.SEEK_END) # указатель в конец файла устанавливается.
#    print('os.SEEK_END = ', os.SEEK_END) # == 2
    end = f.tell()
#    print('end = ', end, ' байт в файле',)
    print('end = ', end, ' bytes in file')
    f.seek(0, os.SEEK_SET) # указатель устанавливается в начало файла.
#    print('os.SEEK_SET = ', os.SEEK_SET) # текстовое значение константы - смысла не имеет его сохранять. == 0
#    data = f.read(4)
#    print('data = ', data) # 'SNSS' value
    magic = struct.unpack(types.int32, f.read(4))[0] # 4 bytes from file, tuple
#    magic = struct.unpack(types.int32, f.read(4)) # tuple 1 item
#    magic_2 = struct.unpack(types.int32, f.read(4))
#    magic = struct.unpack(types.int32, data)[0]
#    print('magic = ', magic, 'magic_2 = ', magic_2, 'all') # me variant
    print('magic = ', magic)
#    magic = magic[0]
#    print('magic = ', magic)
    if magic != SNSS_MAGIC:
        raise Exception("Invalid file header!")
    version = struct.unpack(types.int32, f.read(4))[0]
    print('version = ', version)

    while (end - f.tell()) > 0: # до тех пор, пока не будет достигнут конец файла
        # commandSize is a uint16
        commandSize = struct.unpack(types.uint16, f.read(2))[0] # следующие два байта читаются.
        print('commandSize = ', commandSize)
        if commandSize == 0:
            raise Exception("Corrupted File!")
        # idType is a uint8
        idType = struct.unpack(types.uint8, f.read(1))[0] # читается ещё по одному байту.
        print('idType = ', idType)
        # Size of idType is included in commandSize
        content = f.read(commandSize - 1)
        print('content = ', content)
#        print('content = ', str(content, 'utf-8'))
#        print('content = ', content.decode(encoding='cp866', errors='strict'))
#        print('content = ', content.decode(encoding='cp1251', errors='strict'))
#        print('content = ', content.decode(encoding='utf-8', errors='strict'))
#        print('content = ', content.decode('ascii'))
#        print('content = ', content.decode())
        output.append(SNSSCommand(idType, content))
        output_new.append((idType, content))
        global iterr
        iterr += 1
        print('iterr = ', iterr)

    f.close()
    print('File is close, output = ', output)
    return output, output_new

class SNSSCommand():
    """
    A SNSS command :
        - An Id to identify the content of the payload
        - The payload
    Гм. Идентификатор полезной нагрузки... понятно, что ничего пока не понятно. *мрачно*
    """

    def __init__(self, idType, content):
        self.idType = idType
        self.content = content
#        print('idType = ', idType)
#        print('content = ', content)
        print('iterr init = ', iterr)