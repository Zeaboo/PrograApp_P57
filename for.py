# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:24:26 2021

@author: Usuario
"""

lista1=["R1","R2","R3",'S1','S2']
switches=[]
routers=[]
for i in lista1:
    if "1" in i:
        print(i)
    if 'S' in i:
        switches.append(i)
        print(i)
    if "R" in i:
        routers.append(i)
        print(i)

