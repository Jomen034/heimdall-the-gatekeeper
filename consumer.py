from kafka import KafkaConsumer
from json import loads
import json

consumer = KafkaConsumer("HeimdallGatekeeper",
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset="earliest",
    enable_auto_commit=True
)

for message in consumer:
    print(message.value)
    activities = json.loads(message.value)
    for activity in activities['activities']:
        tables = 
