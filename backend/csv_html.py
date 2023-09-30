from flask import Flask, render_template
import csv
csv_file = "/Users/leem/Downloads/9.17-9.23-Hosting-final.csv"

app = Flask(__name__)

def read_csv(csv_file):
    dataList = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            dataList.append(row)
    for i in range(len(dataList)):
        print(dataList[i])
        
    return dataList

@app.route('/')
def display_csv():
    formatted_data = read_csv(csv_file)
    return render_template("result.html", csv_data=formatted_data)

if __name__ == '__main__':
    app.run(debug=True)
