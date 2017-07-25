#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Cay

@file: Baidu.TranslationByBaidu

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


class TranslationByBaidu:
    
    _translationType = {
        1:{'from':'zh', 'to':'en'},
        2:{'from':'en', 'to':'zh'},
        3:{'from':'zh', 'to':'jp'},
        4:{'from':'jp', 'to':'zh'},
        5:{'from':'zh', 'to':'kor'},
        6:{'from':'kor', 'to':'zh'},
    }
    
    _url = 'http://fanyi.baidu.com/v2transapi'
    _header = 'Mozilla/5.0 (Windows NT 6.1; rv:47.0) Gecko/20100101 Firefox/47.0'
    
    def __init__(self, selector, context):
        self._data = {}
        self._data['from'] = self._translationType[selector]['from']
        self._data['to'] = self._translationType[selector]['to']
        self._data['query'] = context
        self._data['transtype'] = 'translang'
    
    
    def translation(self):
        request = urllib.request.Request(self._url)
        request.add_header('User-Agent', self._header)
        data = urllib.parse.urlencode(self._data).encode(encoding='utf_8', errors='strict')
        response = urllib.request.urlopen(request, data)
        html = response.read().decode('utf-8')
        target = json.loads(html)
        print(target['trans_result']['data'][0]['dst'])


if __name__ == '__main__':
    menu()
    selector = int(input('请选择翻译过程: '))
    context = input('请输入需要翻译的文字: ')
    translationByBaidu = TranslationByBaidu(selector, context)
    translationByBaidu.translation()