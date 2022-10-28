#!/usr/bin/python
from PIL import ImageTk, Image
from math import floor
import os
import json

def create_logo():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    print(current_directory)

    json_file = open('files.json')
    data = json.load(json_file)
    print(data['files'])
    num = data['date_and_time'][1]['num_to_use_file']
    print(num)
    element = 'file_'+str(num)
    file_to_use = data['files'][0][element]
    print(file_to_use)

    file_path = current_directory+"/"+file_to_use
    im = Image.open(file_path)

    width1, height1 = im.size
    ratio = width1/height1
    ratio = round(ratio)
    print(ratio)
    size = 25

    num_to_decide_ratio = 4

    if ratio/2 > 1:
        num_to_decide_ratio = num_to_decide_ratio/(ratio/2)

    if ratio/2 < 1:
        num_to_decide_ratio = num_to_decide_ratio/(ratio*2)

    print("num to decide ratio = " , num_to_decide_ratio)

    new_im = im.resize((round(size*num_to_decide_ratio), round(size)))
    print(new_im.size)

    pix = new_im.load()

    file_of_ascii = open(current_directory+"/new_logo.txt", "w")
    ascii_chars = ".,:;+*?%#@S"
    ascii_chars = list(ascii_chars)
    len_ascii = len(ascii_chars)
    print(ascii_chars)
    width, height = new_im.size
    num_to_multiply = 1

    try:
        for n in range(height):
            for i in range(width):
                pixelRGB = new_im.getpixel((row,h))
                r,g,b = pixelRGB
                brightness = (r+g+b)/3 

    except:
        num_to_multiply = num_to_multiply+1
        n = 0
        i = 0

    for h in range(height):
        for row in range(width):
            pixelRGB = new_im.getpixel((row,h))
            
            if "(" not in str(pixelRGB):
                ascii_to_write = ascii_chars[floor(pixelRGB/(len_ascii*num_to_multiply))]    
                file_of_ascii.write(ascii_to_write)
                continue

            r,g,b = pixelRGB
            brightness = (r+g+b)/3 
            ascii_to_write = ascii_chars[floor(brightness/(len_ascii*num_to_multiply))]
            
            file_of_ascii.write(ascii_to_write)
        file_of_ascii.write("\n")

    file_of_ascii.close()
