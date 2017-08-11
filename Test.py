#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import multiprocessing as mul

<<<<<<< HEAD
from nltk.tkinter import *
import tkinter as tk

=======

def f(x):
    return x ** 2
>>>>>>> 2eff8f6efb19ebfa822dd004f8254c86a9c463f7

pool = mul.Pool(10)

<<<<<<< HEAD
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
=======
ref = pool.map(f, [1,2,3,4,5,6,7,8,9,10])

print ref
>>>>>>> 2eff8f6efb19ebfa822dd004f8254c86a9c463f7
