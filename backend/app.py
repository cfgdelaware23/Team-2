from flask import Flask, request
from csv_html import read_csv, jsonify
app = Flask(__name__)

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