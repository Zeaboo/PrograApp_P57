# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:16:42 2021

@author: Usuario
"""
lista=[]

file=open("devices.txt","r")


for item in file:
    item=item.strip()
    lista.append(item)
    print(item)
file.close()
print(lista)