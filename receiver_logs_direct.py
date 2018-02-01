import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
result = channel.queue_declare()

queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(queue=queue_name, exchange='direct_logs', routing_key=severity)


print(' [*] Waiting for logs. To exit press CTRL+C')


def receive_callback(channel, method, properties, body):
    print(' [X] processed {}:{}'.format(method.routing_key, body))


channel.basic_consume(receive_callback, queue=queue_name, no_ack=True)
channel.start_consuming()
