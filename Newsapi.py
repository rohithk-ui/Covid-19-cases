# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:27:01 2020

@author: Rohit Kumar
"""
from tkinter import *
from newsapi import NewsApiClient
import datetime as dt
import pandas as pd

root = Tk()
root.title('Looking for a specific country?')
e = Entry(root, width = 50, bg="yellow", borderwidth = 5)
e.pack()

def myClick():
    myLabel = Label(root, text = Mainart )
    myLabel.pack()
    
myButton = Button(root, text = "Search", command = myClick)
myButton.pack()




newsapi = NewsApiClient(api_key='3e91d2bc871c48cb9be93f31aae41ea1')
data = newsapi.get_everything(q = 'coronavirus' ,  language = 'en', page_size = 20)

articles = data['articles']
for x, y in enumerate(articles):
    print(f'{x}   {y["title"]}')

Mainart = articles 
root.mainloop()