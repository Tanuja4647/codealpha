import os
import shutil

def organize_files(source_dir):
    # Create folders to organize files
    folders = {
        'Documents': ['.pdf', '.doc', '.docx', '.txt'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.mov', '.avi'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Others': []  # Default folder for files with unknown extensions
    }

    # Iterate over files in the source directory
    for filename in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, filename)):
            file_extension = os.path.splitext(filename)[1].lower()

            # Determine the destination folder based on file extension
            destination_folder = 'Others'  # Default folder
            for folder_name, extensions in folders.items():
                if file_extension in extensions:
                    destination_folder = folder_name
                    break
            
            # Create destination folder if it doesn't exist
            destination_path = os.path.join