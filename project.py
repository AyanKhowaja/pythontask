import os
import time

directory = 'dummy files'
print("Current working directory:", directory)
file_path = os.listdir(directory)
print(file_path)

def delete_all_files_in_directory(directory):
    current_time = time.time()  # Move the assignment inside the function
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            file_modified_time = os.path.getmtime(file_path)
            time_difference = current_time - file_modified_time
            if time_difference > 10:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")

delete_all_files_in_directory(directory)