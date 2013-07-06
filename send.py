'''
Created on 2013-3-25

@author: zhou.zeyong
'''
import pika, logging;

def sendMessage(queueName, content):
    logging.basicConfig()
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue = queueName)
    channel.basic_publish(exchange='', routing_key = queueName, body = content);
    print " [x] Sent %s"%(content);
    connection.close()


if __name__ == "__main__":
    sendMessage("image", "width=440,height=0,type=scale,file=/data/web/src/dmd/image/Public/image/user/20130416/1360041930693600.jpg");
    pass;
