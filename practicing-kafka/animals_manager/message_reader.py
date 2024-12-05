import time

from confluent_kafka import Consumer, KafkaException, KafkaError

# Consumer configuration
conf = {
    'bootstrap.servers': 'kafka:9093',  # Replace with your Kafka broker's address
    'group.id': 'my_consumer_group',         # Consumer group ID
    'auto.offset.reset': 'earliest'          # Start reading from the earliest available message
}

# Create a Consumer instance
consumer = Consumer(conf)

# Subscribe to the topic
consumer.subscribe(['cats-creation'])

# Poll for messages in a loop
try:
    while True:
        msg = consumer.poll(timeout=1.0)  # Poll every 1 second

        if msg is None:
            # No message available within timeout
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition
                print(f"End of partition reached: {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")
            else:
                raise KafkaException(msg.error())
        else:
            # Successfully received a message
            print(f"Received message: {msg.value().decode('utf-8')} from {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")
            time.sleep(0.5)

except KeyboardInterrupt:
    print("Consuming interrupted")

finally:
    # Close the consumer to release resources
    consumer.close()
