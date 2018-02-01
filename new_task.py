import sys
import pika
from random import randint

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)


message = ' '.join(sys.argv[1:]) or "Hello World!"
basic_properties = {
    "delivery_mode": 2
}

for i in range(10):
    message = "Task {} - {}".format(i, ('.' * randint(1,5)))
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=message,
                          properties=pika.BasicProperties(**basic_properties))
    print(" [X] Sent {}".format(message))
connection.close()