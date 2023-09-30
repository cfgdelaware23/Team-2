from flask import Flask, request
from schedule_builder import build_schedule
import json

app = Flask(__name__)

@app.route("/getSchedule", methods=['POST'])
def hello_world():
    content = request.json
    print(content)
    # next step - call Anna's function
    # Extract and print each key-value pair

    for key, value in content.items():
        print(f"Key: {key}")
        print(f"Value: {value}")