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
    csv_file = "/Users/leem/Downloads/filename_14.csv"
    eventsArray = []
    currentWeekday = getCurrentWeekDay()

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        skip = next(csv_reader) 
        for row in csv_reader:
            day = row[0].strip().lower()
            # events are added to a dictionary, that is then appended to a list
            if day == currentWeekday:
                # Day,Time,Location,Title,Host,Volunteers
                event = {
                    'Day': row[0].strip(),
                    'Time': row[1].strip(),
                    'Location': row[2].strip(),
                    'Title': row[3].strip(),
                    'Host': row[4].strip(),
                    'Volunteers': row[5].strip()
                }
                eventsArray.append(event)
    # debugging for the index 
    # for i in range(len(eventsArray)):
    #     print(eventsArray[i])
    return eventsArray

# This function that builds upon reading the csv files and compare both files
# file1 is the main csv file
# file2 is the "recurring" file
def compare(file1, file2):
    data1 = []
    currentWeekday = getCurrentWeekDay()
    with open(file1, 'r')as currFile:
        csv_reader = csv.reader(currFile)
        skip = next(csv_reader) 
        for row in csv_reader:
            day = row[0].strip().lower()
            if day == currentWeekday:
                data1.append(row)
                
    # the sec file with the same title to a list
    combined = []
    with open(file2, 'r')as currFile:
        csv_reader = csv.reader(currFile)
        skip = next(csv_reader) 
        
        for row in csv_reader:
            cellTitle = row[2].strip().lower()
            day = row[0].strip().lower()
            for elem in data1:
                # compares if they both have the same title and occur on  the same day
                if elem[2].strip().lower() == cellTitle and day == currentWeekday:
                    event = {
                        'Day': row[0].strip(),
                        'Time': row[1].strip(),
                        'Location': row[2].strip(),
                        'Title': row[3].strip(),
                        'Host': row[4].strip(),
                        'Volunteers': row[5].strip()
                        # 'Date': row[0].strip(),
                        # 'Time': row[1].strip(),
                        # 'Event': row[2].strip(),
                        # 'Account': row[3].strip(),
                        # 'Recurring': row[4].strip(),
                        # 'Meeting ID': row[5].strip(),
                        # 'Organizer': row[6].strip(),
                        # 'Email': row[7].strip(),
                        # 'Description': row[8].strip(),
                        # 'ACB Media Description': row[9].strip(),
                        # 'ACB Media Link': row[10].strip(),
                        # 'Amazon Call Description': row[11].strip(), 
                        # 'Clubhouse Description': row[12].strip(),
                        # 'Clubhouse Link': row[13].strip(),
                        # 'Zoom Title': row[14].strip(),
                        # 'Zoom Link': row[15].strip(),
                        # 'One tap mobile': row[16].strip(),
                        # 'Phone': row[17].strip(),
                        # 'Passcode': row[18].strip()
                    }
                    combined.append(event)
    return combined


@app.route('/')
def display_csv():
    # sends the intended csv into the index.html file
    file1 = "/Users/leem/Downloads/9.17-9.23-Hosting-final.csv"
    file2 = "/Users/leem/Downloads/filename_14.csv"
    result = compare(file1, file2)
    return render_template("index.html", csv_data=result)

if __name__ == '__main__':
    app.run(debug=True)
