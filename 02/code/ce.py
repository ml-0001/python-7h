#coding:utf-8

"""
代码结构实例
"""

import sys #导入一个'系统'模块,以使用'系统'提供的功能

hi_words = 'Hi!'  #代码中想引用的一段文字定义变量

class CE(object):
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        words = '%s ! My name is %s .' % (hi_words, self.name)
        print(words)

def hi_ce():    #定义了一个功能(函数) , 函数会调用另一个函数
    peter = CE('peter')
    peter.say_hello()

if __name__ == '__main__':
    hi_ce()