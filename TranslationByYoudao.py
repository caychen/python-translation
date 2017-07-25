#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Cay

@file: Youdao.TranslationByYoudao

@email: 412425870@qq.com
'''

import urllib.request
import json


def menu():
    print('1:中文 -> 英文')
    print('2:英文 -> 中文')
    print('3:中文 -> 日文')
    print('4:日文 -> 中文')
    print('5:中文 -> 韩文')
    print('6:韩文 -> 中文')
    pass


class TranslationByYoudao:
    
    _translationType = {
        1:'ZH_CN2EN',
        2:'EN2ZH_CN',
        3:'ZH_CN2JA',
        4:'JA2ZH_CN',
        5:'ZH_CN2KR',
        6:'KR2ZH_CN',
    }
    
    _url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    _header = 'Mozilla/5.0 (Windows NT 6.1; rv:47.0) Gecko/20100101 Firefox/47.0'
    
    def __init__(self, selector, context):
        self._data = {}
        self._data['type'] = self._translationType[selector]
        self._data['i'] = context
        self._data['doctype'] = 'json'
        self._data['xmlVersion'] = '1.8'
        self._data['keyfrom'] = 'fanyi.web'
        self._data['ue'] = 'UTF-8'
        self._data['action'] = 'FY_BY_CLICKBUTTON'
        self._data['typoResult'] = 'true'
        
    
    def translation(self):
        request = urllib.request.Request(self._url)
        request.add_header('User-Agent', self._header)
        data = urllib.parse.urlencode(self._data).encode(encoding='utf_8', errors='strict')
        response = urllib.request.urlopen(request, data)
        html = response.read().decode('utf-8')
        target = json.loads(html)
        print(target['translateResult'][0][0]['tgt'])


if __name__ == '__main__':
    menu()
    selector = int(input('请选择翻译过程: '))
    context = input('请输入需要翻译的文字: ')
    translationByYoudao = TranslationByYoudao(selector, context)
    translationByYoudao.translation()