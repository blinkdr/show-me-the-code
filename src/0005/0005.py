#!/usr/bin/env python

from PIL import Image
import os

W, H = (1136, 640)
def resize_images(dir):
    files = os.listdir(dir)
    for file in files:
        img = Image.open(dir+file)
        width, height = img.size
        w_scale = width / W
        h_scale = height / H
        if w_scale > 1 or h_scale > 1:
            if w_scale < h_scale:
                h = H
                w = int(width/h_scale)
            else:
                w = W
                h = int(height/w_scale)
            img = img.resize((w, h))
        img.save('./out/'+file) 
    return 1   

def check_image(dir):
    files = os.listdir(dir)
    for file in files:
        img = Image.open(dir+file)
        print(img.size)      

if __name__ == "__main__":
    dir = "./images/"
    if resize_images(dir):
        print('done')
    else:
        print('error!')
    check_image(dir)
    check_image('./out/')
    