from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

message = {
    "order_id": 1001,
    "status": "CREATED"
}

producer.send("orders", message)
producer.flush()

print("Event Published")
