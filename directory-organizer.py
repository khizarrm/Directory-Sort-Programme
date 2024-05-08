import os
import shutil
import re

print("File Organizer - Khizar Malik\n\n\n")
home_path = os.path.expanduser("~")
print("Instructions to find the directory path are found in the ReadMe file\n")
filePath = input("Would you like to organize your downloads folder? (yes/no) ")

if filePath.lower() == "yes":
    filePath = os.path.join(home_path, "Downloads")
else:
    filePath = input("What is the path of the directory you would like to organize? ")

destination_folders = {
    'image': os.path.join(home_path, 'Pictures'),
    'document': os.path.join(home_path, 'Documents'),
    'music': os.path.join(home_path, 'Music'),
    'video': os.path.join(home_path, 'Movies')
}

extensions_map = {
    'image': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp', 'tif', 'tiff'],
    'document': ['pdf', 'doc', 'docx', 'txt', 'xls', 'xlsx', 'ppt', 'pptx', 'csv'],
    'music': ['mp3', 'wav', 'aac', 'm4a'],
    'video': ['mp4', 'avi', 'mkv', 'mov']
}

# Create directories if they don't exist
for folder in destination_folders.values():
    if not os.path.exists(folder):
        os.makedirs(folder)

# Mapping extensions to destinations
extension_destinations = {}
for category, extensions in extensions_map.items():
    for extension in extensions:
        extension_destinations[extension] = destination_folders[category]

# List all files in the directory
files = [f for f in os.listdir(filePath) if os.path.isfile(os.path.join(filePath, f))]
pattern = re.compile(r'\.([^.]+)$')

for f in files:
    match = pattern.search(f)
    if match:
        extension = match.group(1).lower()
        if extension in extension_destinations:
            source_path = os.path.join(filePath, f)
            destination_path = os.path.join(extension_destinations[extension], f)
            if not os.path.exists(destination_path):
                shutil.move(source_path, destination_path)
                print(f"Moved {f} to {extension_destinations[extension]}")
            else:
                print(f"File {f} already exists at destination.")
        else:
            print(f"No destination for files with extension: {extension}")
    else:
        print(f"No recognizable extension in file name: {f}")

print("Programme Completed.")
