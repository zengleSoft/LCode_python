#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/6/4

class dummyclass(object):
    def __init__(self):
        self.is_d = True

class childdummyclass(dummyclass):
    def __init__(self,isman):
        self.isman = isman
    @classmethod
    def can_speak(self):
        return True
    @property
    def man(self):
        return self.isman

if __name__ == '__main__':
    object = childdummyclass(True)
    print(object.can_speak())
    print(object.man)
    print(object.is_d)