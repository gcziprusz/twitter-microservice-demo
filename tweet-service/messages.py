import pika

QUEUE_NAME = 'messageQueue'
EXCHANGE_NAME = 'messageExchange'
ROUTING_KEY = 'messageRoutingKey'

def callback(ch, method, properties, body):
    print(f"tweet-service: received {body.decode()}", flush=True)

def consume_messages():
    print('!!!!!!!tweet service: consume_messages RabbitMQ', flush=True)
    # Connect to RabbitMQ
    # try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbitmq',  # Docker service name
        port=5672,                # Default RabbitMQ port
        )
    )
    channel = connection.channel()
    # Declare exchange and queue
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='direct', durable=True)
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=QUEUE_NAME, routing_key=ROUTING_KEY)

    print('Waiting for messages. To exit press CTRL+C', flush=True)

    # Consume messages from the queue
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)

    # Start consuming
    channel.start_consuming()
    # except pika.exceptions.AMQPConnectionError as e:
    #     print(f"Connection failed: {e}", flush=True)
    #     # Detailed error logging
    #     print("Possible issues:", flush=True)
    #     print("- RabbitMQ server not running", flush=True)
    #     print("- Incorrect hostname", flush=True)
    #     print("- Network/firewall blocking connection", flush=True)
    #     print("- Incorrect credentials", flush=True)

if __name__ == "__main__":
    consume_messages()
