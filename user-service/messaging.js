const amqp = require('amqplib');

const QUEUE_NAME = 'messageQueue';
const EXCHANGE_NAME = 'messageExchange';
const ROUTING_KEY = 'messageRoutingKey';

async function publishMessage(message) {
    try {
        // Connect to RabbitMQ server
        const connection = await amqp.connect('amqp://user:password@rabbitmq');
        const channel = await connection.createChannel();

        // Declare exchange and queue
        await channel.assertExchange(EXCHANGE_NAME, 'direct', { durable: true });
        await channel.assertQueue(QUEUE_NAME, { durable: true });

        // Publish the message
        channel.publish(EXCHANGE_NAME, ROUTING_KEY, Buffer.from(message));
        console.log('Sent:', message);

        // Close the connection
        setTimeout(() => {
            connection.close();
        }, 500);
    } catch (error) {
        console.error('Error:', error);
    }
}
module.exports = { publishMessage };
