import pika
import random

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange_type='direct', exchange='direct_logs')


severity_list = ['info', 'warning', 'error']
severity_key = random.randint(0, (len(severity_list)-1))
severity = severity_list[severity_key]
message = '{} any message'.format(severity)

print("[X] Published message with severity {}".format(severity))
channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)
connection.close()
