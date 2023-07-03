import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload

def authenticate():
    credentials_path = 'credentials.json'
    credentials = service_account.Credentials.from_service_account_file(credentials_path, scopes=['https://www.googleapis.com/auth/drive'])
    service = build('drive', 'v3', credentials=credentials)
    return service

def upload_files(service, folder_id, directory_path):
    file_paths = []
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            file_paths.append(file_path)

    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }
        media = MediaFileUpload(file_path)
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        print('File uploaded successfully. File ID:', file.get('id'))

def filescleaner(service, folder_id, directory_path):
    file_names = os.listdir(directory_path)
    deleted_files_list = []

    if file_names:
        print(file_names)
        for file_name in file_names:
            file_path = os.path.join(directory_path, file_name)
            if os.path.isfile(file_path):
                deleted_files_list.append(file_name)
                os.remove(file_path)
                print(f'{file_name} file is deleted')
        print(f'These {len(deleted_files_list)} files are deleted: {deleted_files_list}')
    else:
        print('There are no files')

def main():
    service = authenticate()

    folder_id = "1ac2fCAhhk_PlWwhDJfmp8B73nItvfgfd"
    directory_path ="Dummyfiles"

    upload_files(service, folder_id, directory_path)
    filescleaner(service, folder_id, directory_path)



main()
