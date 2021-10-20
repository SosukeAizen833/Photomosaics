# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:41:38 2021

@author: Space
"""
#%%
from PIL import Image,ImageDraw,ImageFilter
import numpy as np
import math
im = Image.open('input/pexels-limuel-gonzales-6785291.jpg')
im=im.resize((round(im.size[0]*0.5),round(im.size[1]*0.5)))
print(im.size)
cropped_images = []
im.show()
#%%
def create_cropped_images(image,side):
    for i in range(round(image.size[1]/side)):
        row = []
        for j in range(round(image.size[0]/side)):
            x = image.crop((j*side,i*side,(j+1)*side,(i+1)*side))
            row.append(x)
        cropped_images.append(row)

create_cropped_images(im,50)
print(cropped_images[0][0].size)
cropped_images[13][1].show()
#%%
import glob
source_image_list = []
for filename in glob.glob('E:/Adv_Begg/Photomosaics/Pokemon_images/*.png'):#finds all png files
    img=Image.open(filename)
    
    img.convert("RGB")
    crop_img = img.resize((50,50))
    source_image_list.append(crop_img)
print(source_image_list[0].size)

#%%
def get_avg_color_of_single_image(img):

    rgb_list = np.array(img.getdata()).tolist()
    n = len(rgb_list)
    
    r_sum = 0
    g_sum = 0
    b_sum = 0
    for i in range(len(rgb_list)):
        if(isinstance(rgb_list[i], list)):
            r_sum =r_sum+ rgb_list[i][0]
            g_sum =g_sum+ rgb_list[i][1]
            b_sum = b_sum+rgb_list[i][2]
    avg_color = [round(r_sum/n),round(g_sum/n),round(b_sum/n)]
    return avg_color

#print(get_avg_color_of_single_image(cropped_images[5]))
#print(get_avg_color_of_single_image(cropped_images[0]))
def get_avg_of_all(cropped_images):
    average_colors = []
    for x in cropped_images:
        row = []
        for y in x:
            row.append(get_avg_color_of_single_image(y))
        average_colors.append(row)
    return average_colors

#%%

avg_cols = get_avg_of_all(cropped_images)
#%%
def create_pixel_image():
    pixel_im = Image.new('RGB',(cropped_images[0][0].size[0]*len(cropped_images[0]),cropped_images[0][0].size[1]*len(cropped_images)),(255,255,255))
    average_colors = get_avg_of_all(cropped_images);
    print(len(average_colors))
    for i in range(len(cropped_images)):
        for j in range(len(cropped_images[i])):
            each_img = Image.new('RGB',(cropped_images[0][0].size[0],cropped_images[0][0].size[1]),tuple(average_colors[i][j]))
            pixel_im.paste(each_img,(j*each_img.size[0],i*each_img.size[1]))
    return pixel_im


#%%
pixel_im = create_pixel_image()
im.show()
pixel_im.show()

#%%
source_image_avg = []
def calculate_source_avg():
    for i in range(len(source_image_list)):
        source_image_avg.append(get_avg_color_of_single_image(source_image_list[i]))

#%%
calculate_source_avg()
print(len(source_image_avg))
#%%
def find_closest(rgb_average):
    min = float('inf')
    for i in range(len(source_image_list)):
        curr_avg = source_image_avg[i];
        distance = math.sqrt((curr_avg[0]-rgb_average[0])**2+(curr_avg[1]-rgb_average[1])**2+(curr_avg[1]-rgb_average[1])**2)
        if(distance < min):
            min = distance
            closest_img = source_image_list[i]
    return closest_img

#%%
print(len(source_image_list))
average_colors = get_avg_of_all(cropped_images);
#%%
def create_op_image():
    op_img = Image.new('RGB',(cropped_images[0][0].size[0]*len(cropped_images[0]),cropped_images[0][0].size[1]*len(cropped_images)),(255,255,255))
    average_colors = get_avg_of_all(cropped_images);
    #print(average_colors[0][0])
    for i in range(len(average_colors)):
        for j in range(len(average_colors[i])):
            source_img = find_closest(average_colors[i][j])
            op_img.paste(source_img,(j*source_img.size[0],i*source_img.size[1]))
    
    return op_img


op_img = create_op_image()
print(op_img.size)
print(cropped_images[0][0].size[0]*len(cropped_images[0]),cropped_images[0][0].size[1]*len(cropped_images))
#%%
op_img.show()
    
    
    
    
    
    
    
    
    




