import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


def receive_callback(channel, method, properties, body):
    print(" [X] Received {}".format(body))


channel.queue_declare(queue='hello')
channel.basic_consume(receive_callback, queue='hello', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()