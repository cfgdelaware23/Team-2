from flask import Flask, render_template, jsonify
import csv
from datetime import datetime
import pandas

# Initialize the Flask app
app = Flask(__name__)

def getCurrentWeekDay():
    """
    Get the current weekday as a string.

    Returns:
        str: The current weekday.
    """
    dt = datetime.now()
    weekDay = dt.weekday() + 1
    listWeek = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    return listWeek[weekDay]

def excelToCsv():
    """
    Convert an Excel file to CSV format.

    Returns:
        str: The name of the generated CSV file.
    """
    excelFile = "backend/sample file/Copy of Recurring events 2023.xlsx"

    read_file = pandas.read_excel(excelFile)

    csv_file = "fileOutput.csv"
    
    read_file.to_csv (csv_file, index = None, header=True)
    return csv_file
    
def read_csv():
    """
    Read events data from a CSV file.

    Returns:
        list: A list of dictionaries containing event information.
    """
    csv_file = "backend/sample file/filename_14.csv"
    eventsArray = []
    currentWeekday = getCurrentWeekDay()

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        # Skip the header row
        skip = next(csv_reader) 
        for row in csv_reader:
            day = row[0].strip().lower()
            # events are added to a dictionary, that is then appended to a list
            if day == currentWeekday:
                # Extract event information into a dictionary
                event = {
                    'Day': row[0].strip(),
                    'Time': row[1].strip(),
                    'Location': row[2].strip(),
                    'Title': row[3].strip(),
                    'Host': row[4].strip(),
                    'Volunteers': row[5].strip()
                }
                eventsArray.append(event)
    return eventsArray

def compare(file1, file2):
    """
    Compare events between two CSV files.

    Args:
        file1 (str): The main CSV file.
        file2 (str): The "recurring" CSV file.

    Returns:
        list: A list of dictionaries containing combined event information.
    """
    data1 = []
    currentWeekday = getCurrentWeekDay()
    
    # Read data from the main CSV file
    with open(file1, 'r')as currFile:
        csv_reader = csv.reader(currFile)
        # Skip the header row
        skip = next(csv_reader) 
        for row in csv_reader:
            day = row[0].strip().lower()
            if day == currentWeekday:
                data1.append(row)
                
    # Compare events between the two CSV files
    combined = []
    with open(file2, 'r')as currFile:
        csv_reader = csv.reader(currFile)
        # Skip the header row
        skip = next(csv_reader) 
        for row in csv_reader:
            cellTitle = row[2].strip().lower()
            day = row[0].strip().lower()
            for elem in data1:
                # Compare if they both have the same title and occur on the same day
                if elem[2].strip().lower() == cellTitle and day == currentWeekday:
                    # Extract event information into a dictionary
                    event = {
                        'Day': row[0].strip(),
                        'Time': row[1].strip(),
                        'Location': row[2].strip(),
                        'Title': row[3].strip(),
                        'Host': row[4].strip(),
                        'Volunteers': row[5].strip()
                    }
                    combined.append(event)
    return combined


@app.route('/')
def display_csv():
    """
    Display CSV data on a web page.

    Returns:
        str: Rendered HTML template displaying CSV data.
    """
    file1 = "backend/sample file/9.17-9.23-Hosting-final.csv"
    file2 = "backend/sample file/filename_14.csv"
    result = compare(file1, file2)
    return render_template("index.html", csv_data=result)

if __name__ == '__main__':
    app.run(debug=True)
