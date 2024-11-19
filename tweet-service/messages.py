import pika

QUEUE_NAME = 'messageQueue'
EXCHANGE_NAME = 'messageExchange'
ROUTING_KEY = 'messageRoutingKey'

def callback(ch, method, properties, body):
    print(f"tweet-service: received {body.decode()}")

def consume_messages():
    print('consume_messages RabbitMQ')
    # Connect to RabbitMQ
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='rabbitmq-service',  # Docker service name
            port=5672,                # Default RabbitMQ port
            credentials=pika.PlainCredentials('user', 'password')
            )
        )
        channel = connection.channel()
        # Declare exchange and queue
        channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='direct', durable=True)
        channel.queue_declare(queue=QUEUE_NAME, durable=True)
        channel.queue_bind(exchange=EXCHANGE_NAME, queue=QUEUE_NAME, routing_key=ROUTING_KEY)

        print('Waiting for messages. To exit press CTRL+C')

        # Consume messages from the queue
        channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)

        # Start consuming
        channel.start_consuming()
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Connection failed: {e}")
        # Detailed error logging
        print("Possible issues:")
        print("- RabbitMQ server not running")
        print("- Incorrect hostname")
        print("- Network/firewall blocking connection")
        print("- Incorrect credentials")