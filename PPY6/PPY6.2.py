"""
Write a script to handle the folder structure. The user provides folder
names, and the script creates a structure. The script should allow for
deleting and creating structures. Use the knowledge acquired from the
beginning of the course. Use classes, functions, etc. if it is appropriate.
Keep in mind the comfort of using your solution. Recommended module is
os module. You can use other modules. User should be able to input
information about file structure(for example, system asks how many
directories should, user writes 2, then it asks how many directories it
should create in a first one etc.)(2 points)
"""

import os
import shutil

class DirectoryBuilder:
    def __init__(self):
        self.current_directory = os.getcwd()

    def create_directory(self, directory):
        path = os.path.join(self.current_directory, directory)
        os.makedirs(path, exist_ok=True)

    def change_directory(self, directory):
        path = os.path.join(self.current_directory, directory)
        os.chdir(path)
        self.current_directory = os.getcwd()

    def delete_directory(self, directory):
        path = os.path.join(self.current_directory, directory)
        if os.path.exists(path):
            shutil.rmtree(path)

    def check_directory(self):
        print(os.getcwd())

    def check_directory_content(self):
        print(os.listdir(os.getcwd()))

builder = DirectoryBuilder()

builder.create_directory("adf")
builder.delete_directory("adf")

print(builder.current_directory)
print(builder.check_directory_content())