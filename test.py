import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',  # Assuming RabbitMQ is running locally
        port=5672,
        credentials=pika.PlainCredentials('user', 'password')
    )
)
channel = connection.channel()
channel.queue_declare(queue='my_queue')
print("Connection successful!")
connection.close()
