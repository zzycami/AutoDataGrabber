# -*- coding:utf-8 -*-   
'''
Created on 2013-3-19

@author: zhou.zeyong
'''

import os;
from ImageFactory import ImageFactory;



'''confirm that if this file has been dealt'''
def is_deal(fileName):
    attribution = ["_small", "_large", "_middle", "_item_small", "_item_middle", "_item_large", "_200x80", "_232x93"];
    for name in attribution:
        if fileName.find(name) != -1:
            return True;
    return False;

'''resize the images'''
def resize_image_in_folder(path):
    if os.path.isfile(path):
        if is_deal(path):
            return;
        imageFactory = ImageFactory("");
        try:
            imageFactory.getThumbByCut(232, 93, path, "_232x93");
            imageFactory.getThumbByCut(80, 80, path, "_80x80");
        except:
            pass;
    elif os.path.isdir(path):
        files = os.listdir(path);
        for imageFile in files:
            resize_image_in_folder(path + "/" + imageFile);
    else:
        print("the given path is not a folder or a file :%s"%path);
        
        

# test the function
if __name__ == '__main__':
    # constant value define
    IMAGE_ROOT_PATH = "/data/home/dmd-v3/web/src/dmd/image/Public/image/user";
    
    resize_image_in_folder(IMAGE_ROOT_PATH);
