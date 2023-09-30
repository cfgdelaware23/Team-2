from flask import Flask, request

app = Flask(__name__)

@app.route("/getSchedule", methods=['POST'])
def hello_world():
    content = request.json
    print(content)
    return content