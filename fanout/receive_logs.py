import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)
print(" [X] Waiting for logs. To exit press CTRL+C")


def receive_callback(channel, method, properties, body):
    print(" [X] {} - Channel Number: {}".format(body, queue_name))


channel.basic_consume(receive_callback, queue=queue_name, no_ack=True)
channel.start_consuming()
