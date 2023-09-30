from flask import Flask, render_template, jsonify
import csv
from datetime import datetime
import pandas

# sample csv file, will be replaced with the CSV file sent through

app = Flask(__name__)

def getCurrentWeekDay():
    # calculates the next day, this will come in handy when implementing email service automation
    dt = datetime.now()
    weekDay = dt.weekday() + 1
    listWeek = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    return listWeek[weekDay]

def excelToCsv():
    # converts an excel file into csv, expecting an input file
    excelFile = "/Users/leem/Downloads/Copy of Recurring events 2023.xlsx"

    read_file = pandas.read_excel(excelFile)

    csv_file = "fileOutput.csv"
    
    read_file.to_csv (csv_file, index = None, header=True)
    return csv_file
    
def read_csv():
    csv_file = excelToCsv()
    eventsArray = []
    currentWeekday = getCurrentWeekDay()

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        skip = next(csv_reader) 
        for row in csv_reader:
            day = row[0].strip().lower()
            # events are added to a dictionary, that is then appended to a list
            if day == currentWeekday:
                event = {
                    'Date': row[0].strip(),
                    'Time': row[1].strip(),
                    'Event': row[2].strip(),
                    'Account': row[3].strip(),
                    'Recurring': row[4].strip(),
                    'Meeting ID': row[5].strip(),
                    'Organizer': row[6].strip(),
                    'Email': row[7].strip(),
                    'Description': row[8].strip(),
                    'ACB Media Description': row[9].strip(),
                    'ACB Media Link': row[10].strip(),
                    'Amazon Call Description': row[11].strip(), 
                    'Clubhouse Description': row[12].strip(),
                    'Clubhouse Link': row[13].strip(),
                    'Zoom Title': row[14].strip(),
                    'Zoom Link': row[15].strip(),
                    'One tap mobile': row[16].strip(),
                    'Phone': row[17].strip(),
                    'Passcode': row[18].strip()
                }
                eventsArray.append(event)
    # debugging for the index 
    # for i in range(len(eventsArray)):
    #     print(eventsArray[i])
    return eventsArray

    
@app.route('/')
def display_csv():
    # sends the intended csv into the index.html file
    result = read_csv()
    return render_template("index.html", csv_data=result)

if __name__ == '__main__':
    app.run(debug=True)
