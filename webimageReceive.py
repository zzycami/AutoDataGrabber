'''
Created on 2013-4-7

@author: zhou.zeyong
'''
import pika, logging, webImage, send;
import ConfigParser, os
from thumb import ImageFactory

## configuration
config = ConfigParser.ConfigParser()
config.read("%s/config.ini"%(os.path.split(__file__)[0]))
QUEUE_NAME = config.get("queue", "QUEUE_NAME")
HOST = config.get("queue", "HOST")
PORT = config.getint("queue", "PORT")
USER = config.get("queue", "USER")
PASS = config.get("queue", "PASS")
EXCHANGE = config.get("queue", "EXCHANGE")
UPLOAD_PATH = webImage.UPLOAD_PATH

## analyze the parameter
def analyze(param):
    params = param.split(",");
    ret = {};
    for item in params:
        tempValue = item.strip().split("=");
        key = tempValue[0].strip();
        value = tempValue[1].strip();
        ret[key] = value;
    return ret;

## connect
logging.basicConfig()
credentials = pika.PlainCredentials(USER, PASS)
parameters = pika.ConnectionParameters(HOST, PORT, credentials = credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange = EXCHANGE)
channel.queue_declare(queue = QUEUE_NAME)

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body));
    data = analyze(body);
    url = data.get("url");
    fileName = data.get("file_name");
    res = webImage.downloadFile(url, fileName);
    # if download failed skip
    if res == False:
        return;
    
    # After dowload image , then cut the images
    point = fileName.rfind(".");
    extension = fileName[point:len(fileName)];
    
    realPath = UPLOAD_PATH + "/" + fileName;
    if extension != "gif":
        imageFactory = ImageFactory("")
        imageFactory.getStaticThumbByScale(440, realPath,  "_440")
        imageFactory.getStaticThumbByScale(192, realPath,  "_192")
        imageFactory.getStaticThumbByCut(50, 50, realPath,  "_50x50")
        imageFactory.getStaticThumbByCut(180, 180, realPath,  "_180x180")
        imageFactory.getStaticThumbByCut(80, 80, realPath,  "_80x80")
        imageFactory.getStaticThumbByCut(232, 93, realPath,  "_232x93")
    else:
        send.sendMessage("image", "width=440,height=0,type=scale,file=%s"%(realPath));
        send.sendMessage("image", "width=192,height=0,type=scale,file=%s"%(realPath));
        send.sendMessage("image", "width=50,height=50,type=cut,file=%s"%(realPath));
        send.sendMessage("image", "width=180,height=180,type=cut,file=%s"%(realPath));
        send.sendMessage("image", "width=80,height=80,type=cut,file=%s"%(realPath));
        send.sendMessage("image", "width=232,height=93,type=cut,file=%s"%(realPath));

channel.basic_consume(callback, queue=QUEUE_NAME, no_ack=True)
channel.start_consuming()
