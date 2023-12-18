from flask import Flask, render_template, request
import csv

mutualite = Flask(__name__)

def writetocsv(data):
    with open('datamutualite.csv', 'a', newline='') as csv_file:
        fieldnames = ['u_name', 'p1', 'p2']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if csv_file.tell() == 0:
            writer.writeheader()
        writer.writerow(data)

@mutualite.route('/')
def index():
    return render_template('mutualite.html')

@mutualite.route('/process_form', methods=['POST'])
def process_form():
    u_name = request.form['u_name']
    p1 = request.form['p1']
    p2 = request.form['p2']

    writetocsv({'u_name': u_name, 'p1': p1, 'p2': p2})
    print("hi janani")
    return "data stored successfully"

if __name__ == '__main__':
    mutualite.run(debug=True)

    
