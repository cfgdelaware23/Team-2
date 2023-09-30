from flask import Flask, render_template
import csv
from json import dumps
from datetime import datetime
import pandas
# sample csv file, will be replaced with the CSV file sent through
# csv_file = "/Users/leem/Downloads/Copy of Recurring events 2023.xlsx"

app = Flask(__name__)

def getCurrentWeekDay():
    # calculates the next day, this will come in handy when implementing email service automation
    dt = datetime.now()
    weekDay = dt.weekday() + 1
    listWeek = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    return listWeek[weekDay]

def excelToCsv():
    # converts an excel file into csv
    excelFile = "/Users/leem/Downloads/Copy of Recurring events 2023.xlsx"

    read_file = pandas.read_excel(excelFile)

    csv_file = "fileOutput.csv"
    
    read_file.to_csv (csv_file, 
                  index = None,
                  header=True)
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
            # append the next day to the array 
            if day == currentWeekday:
                eventsArray.append(row)
    return eventsArray


@app.route('/')
def display_csv():
    ## sends the intended csv into the index.html file
    result = read_csv()
    return render_template("index.html", csv_data=result)

if __name__ == '__main__':
    app.run(debug=True)
