from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_45539259475-gf8cmqdp1806gct9fh7gppad8lqu1hbi.apps.googleusercontent.com.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = '1PZZXLH8IRRVwJd8JNZR8ekajzQskH-Pa'
file_names = ["undefined.png"]
mime_types = ["image/png"]

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

# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive

# gauth = GoogleAuth()
# gauth.LocalWebserverAuth() # This will open a browser window for authentication

# drive = GoogleDrive(gauth)

# file1 = drive.CreateFile({'title': 'my_file.txt'}) 
# file1.SetContentFile('path/to/your/file.txt') 
# file1.Upload() 
