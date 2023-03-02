from flask import Flask
from flask_cors import CORS
import websocket
import json

from datetime import timezone
import datetime

app = Flask(__name__)
CORS(app, resources={r"/rows/*": {"origins": "http://127.0.0.1:3000"}})

rows = [
        {"pos":"0",
         "date":"20 Apr, 2020",
         "name":"John Doe",
         "shipTo":"Dallas, TX",
         "paymentMethod":"MASTERCARD ⠀•••• 8545",
         "amount": 120.30
         },
         {"pos":"1",
         "date":"16 Mar, 2019",
         "name":"John GoodTwoShoes",
         "shipTo":"Houston, TX",
         "paymentMethod":"VISA ⠀•••• 4521",
         "amount": 60.44
         },
        {"pos":"2",
         "date":"29 Jul, 2020",
         "name":"Ada Lovelace",
         "shipTo":"London, GB",
         "paymentMethod":"VISA ⠀•••• 7586",
         "amount": 84.44
         },
        {"pos":"3",
         "date":"16 Mar, 2019",
         "name":"Elvis Presley",
         "shipTo":"Tupelo, MS",
         "paymentMethod":"VISA ⠀•••• 6352",
         "amount": 312.44
         },
        {"pos":"4",
         "date":"16 Mar, 3033",
         "name":"user12323",
         "shipTo":"North Pole",
         "paymentMethod":"MASTERCARD ⠀•••• 3719",
         "amount": -4654645454.88
         }
    ]

@app.route("/")
def home():
    return "Hello World"

@app.route("/rows", methods=['GET'])
def getRows():
    json_rows = generateJSONFromList(rows)
    log(f"Sent Row Request {len(json_rows)}")
    return json_rows

def generateJSONFromList(list):
    json_str = json.dumps(list)
    log("Generated Rows")
    return json_str

def log(data: str):
    dt = datetime.datetime.now(timezone.utc)
    utc_time = dt.replace(tzinfo=timezone.utc)
    utc_timestamp = round(utc_time.timestamp() * 1000)
    message = "{" + f'\"type":\"Server\",\"data\":\"{data}\",\"date\":\"{utc_timestamp}\"' + "}"
    ws.send(message)

if __name__ == "__main__":
    ws = websocket.WebSocket()
    ws.connect("ws://localhost:8282/process?id=python_example")
    app.run()
