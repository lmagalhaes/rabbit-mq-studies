import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
print(" [*] Waiting for messages. To exit press CTRL+C")


def receive_callback(channel, method, properties, body):
    print(" [X] Received {}".format(body))
    time.sleep(body.count(b'.'))
    print(" [X] Done")
    channel.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_size=1)
channel.basic_consume(receive_callback, queue='task_queue')
channel.start_consuming()
