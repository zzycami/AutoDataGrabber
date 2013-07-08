'''
Created on 2013-4-5
@author: zhou.zeyong
'''
#!/usr/bin/python
# coding:utf-8

import urllib2, os, datetime, stat, time, re
import ConfigParser, os


# config
config = ConfigParser.ConfigParser()
config.read("%s/config.ini"%(os.path.split(__file__)[0]))
UPLOAD_PATH = config.get("fold", "UPLOAD_PATH")


def renameFile(fileName, addtion):
    point = fileName.rfind(".");
    extension = fileName[point:len(fileName)];
    return fileName[0:point] + addtion + extension;
    
    
def makeSavePath():
    now = datetime.datetime.now()
    dayDir = now.strftime("%Y%m%d")
    uploadDir = UPLOAD_PATH + "/" + dayDir
    if os.path.exists(uploadDir) == False:
        try:
            os.mkdir(uploadDir);
            os.chmod(uploadDir, stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO);
        except:
            print("make folder %s failed."%(uploadDir));
            return;
    return dayDir;

def microtimeFloat():
    gmTime = int(time.time());
    microtime = datetime.datetime.now().microsecond*100;
    return str(gmTime) + str(microtime);


def getWebImageName(url):
    # check the url
    if re.match(r"/^(https?|ftp):\/\/.+\.([a-zA-Z0-9]+)$/", url):
        return False
    # get the http header
    header = urllib2.urlopen(url).headers
    ext = header["Content-Type"].split("/")[1]
    if ext == "jpeg":
        ext = "jpg"
    
    # create the fold whitch is ready for save the image
    path = "%s/%s.%s"%(makeSavePath(), microtimeFloat(), ext)
    return path

def getImageExtension(fm):
    if fm == "JPEG":
        return "jpg";
    elif fm == "PNG":
        return "png";
    elif fm == "GIF":
        return "gif";
    elif fm == "BMP":
        return "bmp";

def downloadFile(url, fileName):
    # Get the image data from web
    try:
        socket = urllib2.urlopen(url);
        data = socket.read();
        socket.close();
    except:
        print("download image from %s failed"%(url));
        return False;
    
    '''
    # Get the Image object from the image data
    try:
        image = Image.open(StringIO.StringIO(data));
    except:
        print("the url is not a image");
        return False;
    '''
    
    
    #save the image
    # use PIL to save the image, when the image is gif image, it will lose the other frame
    fileName = UPLOAD_PATH + "/" + fileName;
    #image.save(fileName);
    try:
        with open(fileName, "wb") as image:
            image.write(data);
        print("download and save image at %s"%(fileName));
    except:
        print("save file %s failed"%(fileName));
        return;
    
if __name__ == "__main__":
    #downloadFile("http://img.hb.aicdn.com/1f42fc3aceb2608dbe08255db5c17107a8565ab2fb7da-Fa9YYz_fw580", "test/test.jpg");
    getWebImageName("http://img.hb.aicdn.com/1f42fc3aceb2608dbe08255db5c17107a8565ab2fb7da-Fa9YYz_fw580")
