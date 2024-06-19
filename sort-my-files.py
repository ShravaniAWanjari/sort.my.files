import os
import shutil
import datetime

source_folder_1 = #"C:/Users/OneDrive/Desktop" Change the path  according to your file system
source_folder_2 = #"C:/Users/Downloads"

destination_folder_photos = #"C:/Users/Documents/All photos"
destination_folder_documents = #"C:/Users/Documents/All Documents"
destination_folder_installed = #"C:/Users/Documents/Installed stuff"
destination_folder_projects = #"C:/Users/Documents/Project files"

DESTINATION_FOLDERS = {
    'Photos': {
        'folder': destination_folder_photos,
        'extensions': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg']
    },

    'Documents': {
        'folder': destination_folder_documents,
        'extensions': ['.pdf', '.docx', '.xlsx', '.pptx', '.txt'] 
    },

    'Installed': {
        'folder': destination_folder_installed,
        'extensions': ['.exe']  
    },

    'Projects': {
        'folder': destination_folder_projects,
        'extensions': ['.ipynb', '.py', '.css', '.json', '.php', '.html', '.js', 
                       '.blend', '.asset', '.prefab', '.cs', '.mat', '.shader', '.anim']
    }
}

def get_all_files(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

all_files = get_all_files(source_folder_1) + get_all_files(source_folder_2)

def move_files(files, destination_folders):
    for file in files:
        file_extension = os.path.splitext(file)[1].lower()
        for category, data in destination_folders.items():
            if file_extension in data['extensions']:
                destination_folder = data['folder']
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                shutil.move(file, os.path.join(destination_folder, os.path.basename(file)))
                break

move_files(all_files, DESTINATION_FOLDERS)

all_files = get_all_files(source_folder_1) + get_all_files(source_folder_2)
move_files(all_files, DESTINATION_FOLDERS)
