#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

a = 5

class func(object):

    def __init__(self):
        pass

    def add(self):
        a = 6
        return a + 3


f = func()
print f.add()