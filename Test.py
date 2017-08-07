#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

a = 5
class Fjs(object):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print "said by : ", self.name
        print a
    def fjs(self, name):
        if name == self.name:
            print "yes"
        else:
            print "no"


class Wrap_Fjs(object):
    def __init__(self, fjs):
        self._fjs = fjs

    def __getattr__(self, item):
        if item == "hello":
            print "调用hello方法了"
        elif item == "fjs":
            print "调用fjs方法了"
        return getattr(self._fjs, item)


fjs = Wrap_Fjs(Fjs("fjs"))
fjs.hello()
fjs.fjs("fjs")
