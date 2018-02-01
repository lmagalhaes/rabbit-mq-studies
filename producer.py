import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

message = 'Hello World!'
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body=message)

print(" [X] Sent '{}'".format(message))

connection.close()