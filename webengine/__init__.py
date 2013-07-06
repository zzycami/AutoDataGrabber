import os
# get the root of current file
path = os.path.split(__file__)[0]
moduleList = os.listdir(path)
for module in moduleList:
    if os.path.isfile(module):
        fileName, extension = os.path.splitext(module)
        if fileName != "__init__" and extension == ".py":
            IMPORT_STR = "import %s"%(fileName)
            exec IMPORT_STR
    
