from flask import Flask, render_template
import csv
from json import dumps
# sample csv file, will be replaced with the CSV file sent through
csv_file = "/Users/leem/Downloads/9.17-9.23-Hosting-final.csv"

app = Flask(__name__)

def read_csv(csv_file):
    dataList = []
    with open(csv_file, 'r') as file:
        # loops through the csv file and format each row into an array index
        csv_reader = csv.reader(file)
        for row in csv_reader:
            dataList.append(row)
    # outputs to console for debugging
    # NEEDS TO BE TAKEN OUT LATER
    for i in range(len(dataList)):
        print(dataList[i])
        
    json_result = dumps(dataList)
    return json_result

@app.route('/')
def display_csv():
    ## sends the intended csv into the index.html file
    json_result = read_csv(csv_file)
    return render_template("index.html", csv_data=json_result)

if __name__ == '__main__':
    app.run(debug=True)
