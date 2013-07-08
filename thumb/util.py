'''
Created on 2013-3-21

@author: zhou.zeyong
'''
import os;
'''
delete the directory tree
path the relative path of the folder you want delete
'''
def delete_file_folder(path):
    # get the absolute path of the folder which will be deleted
    folder_path =  path;
    if os.path.isfile(folder_path):
        # if the given path is a file, delete it
        try:
            os.remove(folder_path);
            #print(folder_path);
        except:
            pass;
    elif os.path.isdir(folder_path):
        # if the given path is a folder, list and delete the files
        for file_name in os.listdir(path):
            delete_file_folder(path + "/" + file_name);
        try:
            os.rmdir(folder_path);
        except:
            pass;
    else:
        print("The given parameter is not file or folder:%s"%(folder_path));
    
        

# test the function
if __name__ == '__main__':
    delete_file_folder("image/HTML5CANVAS");
            
