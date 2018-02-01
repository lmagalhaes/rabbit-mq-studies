import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')
result = channel.queue_declare(exclusive=True)
channel.queue_bind(exchange='logs', queue=result.method.queue)

message = "My beautiful message"
channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message)

print(" [X] Sent {}".format(message))
connection.close()
