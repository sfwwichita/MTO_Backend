from flask import Flask, render_template, request, send_from_directory, jsonify
from googleapiclient.http import MediaFileUpload
from Google import Create_Service
import os
import csv

app = Flask(__name__, static_folder="static")

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/')
def index():
    return render_template('Submit.html')

Color = ''
Icon  =''
Option = ''

@app.route('/process_data', methods=['POST'])
def process_data():
    session_data = request.get_json()
    # Do something with the session data
    print(session_data)
    return jsonify({'message': 'Data received'})

@app.route('/submit', methods=['POST'])
def submit():
    session_data = request.get_json()
    color = session_data.get('color')
    option = session_data.get('option')
    icon = session_data.get('icon')
    print(color, option, icon)

    # Write to Data.csv
    with open('Data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([color, option, icon])

    CLIENT_SECRET_FILE = 'client_secret_45539259475-gf8cmqdp1806gct9fh7gppad8lqu1hbi.apps.googleusercontent.com.json'
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    folder_id = '1PZZXLH8IRRVwJd8JNZR8ekajzQskH-Pa'
    file_names = ["Data.csv"]
    mime_types = ["text/csv"]

    for file_name, mime_type in zip(file_names, mime_types):
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }

        media = MediaFileUpload('{0}'.format(file_name), mimetype=mime_type)

        service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()

    print("doing something")
    confirmation_html = render_template("Confirmation.html")
    return jsonify({'message': 'Color submitted successfully!', 'confirmation_html': confirmation_html})

if __name__ == '__main__':
    app.run(debug=True)
