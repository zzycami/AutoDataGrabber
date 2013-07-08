'''
Created on 2013-3-20

@author: zhou.zeyong
'''
import images2gif, os, shutil;
import Image;

class ImageFactory:
    imageRootPath = "";
    #IMAGE_FORMAT = {"JPEG":".jpg", "GIF":".gif", "PNG":".png"};
    
    def __init__(self, imageRootPath):
        self.imageRootPath = imageRootPath;
        
    def renameFile(self, fileName, addtion):
        point = fileName.rfind(".");
        extension = fileName[point:len(fileName)];
        return fileName[0:point] + addtion + extension;
    
    ##
    # resize the image with the given width
    # fileName the image file name
    # typeAdd when the image had been finishing dealing the image
    # and save the file ,the typeAdd will be added to the file name
    def getThumbByScale(self,  width, fileName, typeAdd):
        imagePath = self.imageRootPath + fileName;
        try:
            image = Image.open(imagePath);
        except:
            print("the given parameter imagePath is wrong!");
            return;

        imageFormat = image.format;
        # if the size of the image is smaller than the given width, give up, copy the file
        if image.size[0] < width:
            desFile = self.renameFile(imagePath, typeAdd);
            shutil.copy(imagePath, desFile);
            print("the source image size is smaller than ordered size, copy this image, file name:%s"%(desFile));
            return;
        
        self.getStaticThumbByScale(width, fileName, typeAdd);
        
        
            
            
    ##
    # resize the image with the given width
    # fileName the image file name
    # typeAdd when the image had been finishing dealing the image
    # and save the file ,the typeAdd will be added to the file name
    def getStaticThumbByScale(self, width, fileName, typeAdd):
        width = int(width);
        # get the source image size and calculate the scale
        if os.path.isfile(fileName):
            imagePath = fileName;
        else:
            imagePath = self.imageRootPath + fileName;
        try:
            image = Image.open(imagePath);
        except:
            print("the given parameter imagePath is wrong!");
            return;
            
        sourceWidth, sourceHeight = image.size;
        scale = width/float(sourceWidth);
        
        # calculate the destination image size
        desWidth = width;
        desHeight = int(sourceHeight*scale);
        image = image.resize((desWidth, desHeight), Image.ANTIALIAS);
        # save the image
        print("scale with thumb width %s, save at %s"%(width, self.renameFile(fileName, typeAdd)));
        image.save(self.renameFile(imagePath, typeAdd));
    
    
    def getThumbByCut(self, width, height, fileName, typeAdd, scale = 1):
        imagePath = self.imageRootPath + fileName;
        try:
            image = Image.open(imagePath);
        except:
            print("the given parameter imagePath is wrong!");
            return;

        imageFormat = image.format;
        
        # if the size of the image is smaller than the given width, copy this file
        if image.size[0] < width:
            desFile = self.renameFile(imagePath, typeAdd);
            shutil.copy(imagePath, desFile);
            print("the source image size is smaller than ordered size, copy this image, file name:%s"%(desFile));
            return;
        
        self.getStaticThumbByCut(width, height,  fileName, typeAdd, scale);

        
    def getStaticThumbByCut(self, width, height, fileName, typeAdd, scale = 1):
        width = int(width);
        #get the source image size
        if os.path.isfile(fileName):
            imagePath = fileName;
        else:
            imagePath = self.imageRootPath + fileName;
        try:
            image = Image.open(imagePath);
        except:
            print("the given parameter imagePath is wrong!");
            return;
        
        sourceWidth, sourceHeight = image.size;
        #calculate the parameter
        sourceScale = sourceWidth/float(sourceHeight);
        cutScale = width/float(height);
        cutWidth = 0;
        cutHeight = 0;
        if cutScale < sourceScale:
            cutHeight = sourceHeight;
            cutWidth = sourceHeight*cutScale*scale;
        else:
            cutWidth = sourceWidth;
            cutHeight = sourceWidth/cutScale*scale;
        cutWidth = int(cutWidth);
        cutHeight = int(cutHeight);
        cutX1 = (sourceWidth - cutWidth)/2;
        cutY1 = (sourceHeight - cutHeight)/2;
        cutX2 = cutX1 + cutWidth;
        cutY2 = cutY1 + cutHeight;
        rectangle = (cutX1, cutY1, cutX2, cutY2);
        # cut the image
        image = image.crop(rectangle);
        # resize the image
        image = image.resize((width, height), Image.ANTIALIAS);
        # save the image
        print("cut with thumb width %s, save at %s"%(width, self.renameFile(fileName, typeAdd)));
        image.save(self.renameFile(imagePath, typeAdd));
        

# test the function
if __name__ == '__main__':
    imageFactory = ImageFactory("");
    width = 400;
    height = 80;
    imageFactory.getStaticThumbByScale(width, "D:/GithubRepository/web/src/dmd/image/Public/image/user/20130708/137326829078500000.png", "_%s"%(width));