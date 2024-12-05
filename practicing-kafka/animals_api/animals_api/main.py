from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from confluent_kafka import Producer
import json
import logging

# FastAPI app initialization
app = FastAPI()

# Kafka producer configuration
producer_config = {
    'bootstrap.servers': 'kafka:9093',  # Kafka broker address
}

# Create Kafka Producer
producer = Producer(producer_config)

# Kafka topic
topic = 'cats-creation'


# Define Enum for allowed cat colors
class CatColor(str, Enum):
    red = "red"
    green = "green"
    blue = "blue"
    white = "white"
    black = "black"


# Define Pydantic model for request body
class CatRequest(BaseModel):
    cat: CatColor  # Single cat color (e.g., red, black, green)


# Function to send message to Kafka
def send_to_kafka(message: dict):
    try:
        # Produce the message to Kafka topic
        producer.produce(topic, json.dumps(message))
        producer.flush()  # Ensure the message is sent
        logging.info(f"Message sent to {topic}: {message}")
    except Exception as e:
        logging.error(f"Failed to send message to Kafka: {e}")


# POST endpoint to receive cat type and send the event to Kafka
@app.post("/cat")
async def create_cat_event(cat_request: CatRequest):
    # Construct message to send to Kafka
    message = {
        "event": "cat_creation",
        "cat": cat_request.cat,
        "status": "created"
    }

    # Send the message to Kafka
    send_to_kafka(message)

    return {"message": "Cat event created and sent to Kafka", "data": message}
