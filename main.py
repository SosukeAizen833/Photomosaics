# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:41:38 2021

@author: Space
"""

from PIL import Image,ImageDraw
im = Image.open('input/pexels-limuel-gonzales-6785291.jpg')

resized_im = im.resize((round(im.size[0]*0.5),round(im.size[1]*0.5)))
#resized_im.thumbnail((200,200))

resized_im.thumbnail((200,200))
print(resized_im.size)
draw = ImageDraw.Draw(resized_im)
x = resized_im.size[0]
y = resized_im.size[1]
draw.line((x/4,y/6,3*x/4,y/6),fill=128)
draw.line((x*3/4,y/6,3*x/4,3*y/4),fill=128)
draw.line((3*x/4,3*y/4,x/4,3*y/4),fill=128)
draw.line((x/4,3*y/4,x/4,y/6),fill=128)


resized_im.show()
