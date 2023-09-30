from flask import Flask, request
from schedule_builder import build_schedule
from csv_html import read_csv, jsonify
from outputToCSV import convert_to_csv
import json

app = Flask(__name__)

volunteers = {}
events = {}

@app.route("/getSchedule", methods=['POST'])
def hello_world():
    content = request.json
    print(content)
    # next step - call Anna's function
    # Extract each key-value pair for volunteer and format it for 
    # build_schedule function
    for volunteer in content['volunteerData']:
        name = volunteer['name']
        skills = set(volunteer['skills'])
        availability = {}
        availability['monday'] = volunteer['monday']
        availability['tuesday'] = volunteer['tuesday']
        availability['wednesday'] = volunteer['wednesday']
        availability['thursday'] = volunteer['thursday']
        availability['friday'] = volunteer['friday']
        availability['saturday'] = volunteer['saturday']
        availability['sunday'] = volunteer['sunday']
        
        volunteers[name] = [skills, availability]

    for event in content["eventData"]:
        skill = set(None)
        name = event['eventName']
        day = event['day']
        meetingID = event['meetingID']
        organizer = event['organizer']
        account = event['account']
        recurrence = event['recurrence']
        time = event['time']
        num_volunteers = None

        events[name] = [skill, day, time, num_volunteers, organizer, meetingID, 
                        account, recurrence]
    
    # call build_schedule
    schedule_list = build_schedule(events, volunteers)
    schedule_cvs = convert_to_csv(schedule_list)
    

@app.route('/get-events', methods = ['GET'])
def getSelectedEvents():
    filteredArray = read_csv()
    return jsonify(filteredArray)