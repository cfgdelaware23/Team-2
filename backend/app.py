from flask import Flask, request
from schedule_builder import build_schedule
from csv_html import read_csv, jsonify
from outputToCSV import convert_to_csv

app = Flask(__name__)

# Dictionary containing volunteer data
volunteers = {}
# Dictionary containing event data
events = {}

@app.route("/getSchedule", methods=['POST'])
def generate_schedule():
    content = request.json
    # Extract each key-value pair from the json for each volunteer and 
    # format it for the build_schedule function
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

    # Extract each key-value pair from the json for each event and 
    # format it for the build_schedule function
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

        # Add finalized event details to dictionary of all events
        events[name] = [skill, day, time, num_volunteers, organizer, meetingID, 
                        account, recurrence]
    
    # Call build_schedule function to return a row output for final schedule
    schedule_list = build_schedule(events, volunteers)
    # Convert schedule to CSV for the event schedule spreadsheet
    schedule_csv = convert_to_csv(schedule_list)

    # Return the final schedule
    return {
        "schedule": schedule_csv
    }
    

@app.route('/get-events', methods = ['GET'])
def getSelectedEvents():
    filteredArray = read_csv()
    return jsonify(filteredArray)