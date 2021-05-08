from typing import Optional, List
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from kafka import KafkaProducer
import uvicorn
import json

class Activities(BaseModel):
    operation: str
    table: str
    col_names: List[str]
    col_types: List[str]
    col_values: List


class Payload(BaseModel):
    activities: List[Activities]


app = FastAPI()

@app.post('/activities')
async def update_activities(activities: Activities):
    json_form = jsonable_encoder(activities)
    print(json_form)
    results_in_string = json.dumps(json_form).encode('utf-8')
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    producer.send('HeimdallGatekeeper', results_in_string)
    return {'message': 'success', 'payload': json_form}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
