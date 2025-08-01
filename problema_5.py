"""
Write a Python script that must recursively search within {start_directory} and all its subdirectories for all files (not directories)
that contain {search_name} in their name.
The value for the {search_name} and {start_directory} will be read from the keyboard.
The output should contain a list of full paths with all the files that matched the {search_name}.

Args:
    - search_name: A string representing the text to be searched for in filenames.
    - start_directory: The path to a directory where the search will begin.

Returns: The script will display the full paths to the found files, each on a new line.

Error Handling:
    - The script will display an error message and exit if essential inputs (search_name or start_directory)
      are empty or only contain whitespace when read from the keyboard.
    - An error message will be shown if the provided start_directory does not exist or is not a valid directory.

EXAMPLE:
    Structure model:
    test_search/
    ├── main_document_workshop.txt
    ├── workshop_archive.zip
    ├── images/
    │   ├── vacation_photo_workshop.jpg
    │   ├── screenshot.png
    │   └── another_document.txt
    └── project/
        ├── source_code/
        │   ├── main_module_workshop.py
        │   └── document_utils.py
        └── README_project_workshop.md

    If we search for the word "workshop" within the 'test_search/' directory,
    the script should output the following full paths:
        test_search/main_document_workshop.txt
        test_search/workshop_archive.zip
        test_search/images/vacation_photo_workshop.jpg
        test_search/project/source_code/main_module_workshop.py
        test_search/project/README_project_workshop.md
"""

# Solution:

import os

def recursively_find_file(search_name:str, start_directory:str):
    if not name_to_search or not directory_to_start:
        print("Error: Search name and start directory cannot be empty or just whitespace.")
        return None

    if not os.path.isdir(start_directory):
        print(f"Error: Directory '{start_directory}' does not exist or is not valid.")
        return None

    found_files = []
    for root, dirs, files in os.walk(start_directory):
        for filename in files:
            if search_name in filename:
                full_path = os.path.join(root, filename)
                found_files.append(full_path)

    if found_files:
        print(f"Files found containing '{search_name}' in their name:")
        for file_path in found_files:
            print(file_path)
    else:
        print(f"No files found containing '{search_name}' in their name in directory '{start_directory}'.")

if __name__ == "__main__":
    # Good practice to eliminate whitespaces
    name_to_search = input("Enter the text to search for in filenames: ").strip()
    directory_to_start = input("Enter the directory path to start searching from: ").strip()

    recursively_find_file(name_to_search, directory_to_start)
