from flask import Flask, request
from schedule_builder import build_schedule
import json

app = Flask(__name__)

volunteers = {}
events = {}

@app.route("/getSchedule", methods=['POST'])
def hello_world():
    content = request.json
    print(content)
    # next step - call Anna's function
    return content

@app.route('/get-events', methods = ['GET'])
def getSelectedEvents():
    filteredArray = read_csv()
    return jsonify(filteredArray)