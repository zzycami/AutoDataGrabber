'''
Created on 2013-3-25

@author: zhou.zeyong

used to parse a string to parameters
'''
def analyze(param):
    params = param.split(",");
    ret = {};
    for item in params:
        tempValue = item.strip().split("=");
        key = tempValue[0].strip();
        value = tempValue[1].strip();
        ret[key] = value;
    return ret;
    

if __name__ == "__main__":
    str = "width=198,height=300,type=scale,file=D:\Github\web\src\dmd\image\Public\image\user\20130328\136445032464812000.jpg";
    values = analyze(str);
    print(values["file"]);
