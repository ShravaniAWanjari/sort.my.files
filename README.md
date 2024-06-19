# sort.my.files
This Python script helps organize files from source folders into designated destination folders based on their file extensions. It's a convenient way to keep your files tidy and easily accessible.

## Overview

The File Sorter script automates the process of sorting files from multiple source folders and moving them to specific destination folders based on their file types. It simplifies the task of organizing files by categorizing them into folders such as Photos, Documents, Installed, and Projects.

## Features

- **Automated Sorting:** Files are automatically sorted based on their file extensions.
- **Customizable:** Easily customize destination folders and file extensions according to your preferences.
- **Efficient:** Saves time and effort by streamlining the file organization process.

## Usage

1. **Clone the Repository:** Clone this repository to your local machine using the following command:

    ```bash
    git clone https://github.com/ShravaniAWanjari/sort.my.files.git
    ```

2. **Set Source and Destination Folders:** Open the `sort-my-file.py` script and set the source and destination folders according to your requirements.

3. **Run the Script:** Execute the script by running the following command:

    ```bash
    python sort-my-files.py
    ```

4. **Sit Back and Relax:** Let the code do the work for you! Your files will be neatly organized into the specified destination folders.

## Customization

- **Source Folders:** Add or remove source folders by modifying the `source_folders` list in the script.
- **Destination Folders:** Customize destination folders by updating the `DESTINATION_FOLDERS` dictionary in the script. Specify the folder paths and file extensions for each category as per your preference.

## Example

Suppose you have files scattered across different source folders such as Downloads and Desktop. Running the File Sorter script will gather these files and categorize them into folders like Photos, Documents, Installed, and Projects based on their file types. For instance, image files will be moved to the Photos folder, documents to the Documents folder, executables to the Installed folder, and project files to the Projects folder.

