# pip install google-api-python-client

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account



# Replace 'FOLDER_NAME' with the name you want to give your new folder
folder_name = 'images'


# setup google drive
credentials = service_account.Credentials.from_service_account_file(
        'credentials.json', scopes=['https://www.googleapis.com/auth/drive']
    )
service = build("drive", "v3", credentials=credentials)
folder_metadata = {
    'name': folder_name,
    "parents": ['1Oj84uxtU9ScncaTeolQcFnMcF4MSHD2w'],
    'mimeType': 'application/vnd.google-apps.folder'
}

# create folder 
new_folder = service.files().create(body=folder_metadata).execute()

#upload file inside the folder
file_metadata = {'name': 'image.png', 'parents': [new_folder['id']]}
media = MediaFileUpload('image.png')
file = service.files().create(body=file_metadata, media_body=media).execute()

# list the file inside of the folder
results = service.files().list(q=f"'{new_folder['id']}' in parents", fields="files(name)").execute()
items = results.get('files', [])
print(f"Files inside the folder , {items}")