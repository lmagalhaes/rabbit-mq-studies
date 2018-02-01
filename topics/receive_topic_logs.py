import pika
import sys


connections = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connections.channel()

result = channel.queue_declare()
queue_name = result.method.queue

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for routing_key in binding_keys:
    channel.queue_bind(queue=queue_name, exchange='topic_logs', routing_key=routing_key)


def receive_callback(channel, method, properties, body):
    print(' [X] {}:{}'.format(method.routing_key, body))


print(' [*] Waiting for logs. To exit press CTRL+C')
channel.basic_consume(receive_callback, queue=queue_name, no_ack=True)
channel.start_consuming()
