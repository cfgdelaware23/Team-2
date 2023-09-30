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
    # print(content)
    # next step - call Anna's function
    # Extract each key-value pair for volunteer and format it for 
    # build_schedule function
    for volunteer in content['volunteerData']:
        name = volunteer['name']
        skills = set(volunteer['skills'])
        availability = {}
        availability['Monday'] = volunteer['monday']
        availability['Tuesday'] = volunteer['tuesday']
        availability['Wednesday'] = volunteer['wednesday']
        availability['Thursday'] = volunteer['thursday']
        availability['Friday'] = volunteer['friday']
        availability['Saturday'] = volunteer['saturday']
        availability['Sunday'] = volunteer['sunday']
        
        volunteers[name] = [skills, availability]

    for event in content["eventData"]:
        skill = set(event["skillsNeeded"])
        name = event['eventName']
        day = event['day']
        meetingID = event['meetingID']
        organizer = event['organizer']
        account = event['account']
        recurrence = event['recurrence']
        time = event['time']
        num_volunteers = 2

        events[name] = [skill, day, time, num_volunteers, organizer, meetingID, 
                        account, recurrence]
    
    # call build_schedule
    schedule_list = build_schedule(events, volunteers)
    schedule_csv = convert_to_csv(schedule_list)

    # print(schedule_csv)
    return {
        "schedule": schedule_csv
    }
    

@app.route('/get-events', methods = ['GET'])
def getSelectedEvents():
    filteredArray = read_csv()
    return jsonify(filteredArray)