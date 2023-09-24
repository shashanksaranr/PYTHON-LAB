import os
from zipfile import ZipFile

# Give the path where the zip file should be created
with ZipFile("C:\\Users\\HP\\Desktop\\PROGRAMMING\\documents.zip", 'w') as zip:
    # Give the path of files which are need to be zipped
    for folder_name, f_name, file_names in os.walk('C:\\Users\\HP\\Desktop\\PROGRAMMING\\ABC'):
        for file in file_names:
            file_path = os.path.join(folder_name, file)
            zip.write(file_path, os.path.basename(file_path))

            print("Zip File Created!")
