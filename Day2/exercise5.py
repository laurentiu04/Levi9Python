"""
Problem 5.
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

from pathlib import Path

def recursive_search(dir, word):
    try:
        # print("Searching " + dir + ":")
        p = Path(dir)
        for x in p.iterdir():
            if not x.is_dir():
                if x.name.find(word) != -1:
                    print("\t" + dir + "/" + x.relative_to(start_directory).name)
            else: 
                recursive_search(dir + "/" + x.name, word)
    except FileNotFoundError as error:
        print("Error while trying to search directory "  + "'" + dir + "': "  + error.strerror)

start_directory = input("Start directory: ")
if not len(start_directory.strip()):
    print("Error: Start directory cannot be empty! Exiting...")
    quit()
word = input("Search word: ")
if not len(word.strip()):
    print("Error: Search word cannot be empty! Exiting...")
    quit()

recursive_search(start_directory, word)


