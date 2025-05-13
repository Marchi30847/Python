import os
import shutil


class DirectoryBuilder:
    def __init__(self):
        self.current_directory = os.getcwd()
        self.history = [self.current_directory]

    def create_directory(self, directory_name):
        path = os.path.join(self.current_directory, directory_name)

        if os.path.exists(path):
            raise FileExistsError(f"Directory '{directory_name}' already exists.")

        os.makedirs(path)
        print(f"Directory '{directory_name}' created.")
        self.change_directory(directory_name)

    def delete_directory(self, directory_name):
        path = os.path.join(self.current_directory, directory_name)
        if os.path.exists(path):
            shutil.rmtree(path)
            print(f"Directory '{directory_name}' deleted.")
        else:
            raise FileNotFoundError(f"Directory '{directory_name}' doesn't exist.")

    def change_directory(self, directory_name):
        if directory_name == "..":
            if len(self.history) > 1:
                self.history.pop()
                self.current_directory = self.history[-1]
                os.chdir(self.current_directory)
                print(f"Returned to: {self.current_directory}")
            else:
                raise FileNotFoundError(f"Directory '{directory_name}' does not exist.")
        else:
            path = os.path.join(self.current_directory, directory_name)
            if os.path.isdir(path):
                self.current_directory = path
                self.history.append(path)
                os.chdir(self.current_directory)
                print(f"Moved to: {self.current_directory}")
            else:
                print(f"Directory '{directory_name}' not found.")

    def list_directory_content(self):
        print(f"\nCurrent directory: {self.current_directory}")
        content = os.listdir(self.current_directory)
        if content:
            for item in content:
                print(f"- {item}")
        else:
            raise FileNotFoundError(f"Directory '{self.current_directory}' is empty.")

    def start(self):
        while True:
            print("\nCurrent directory:", self.current_directory)
            print("Choose an option:")
            print("1. Create and enter a new directory")
            print("2. Delete a directory")
            print("3. List contents of current directory")
            print("4. Change directory to")
            print("5. Exit")

            choice = input("Enter your choice: ").strip()

            match choice:
                case "1":
                    dir_name = input("Enter new directory name: ").strip()
                    try:
                        self.create_directory(dir_name)
                    except FileExistsError as e:
                        print(e)
                case "2":
                    dir_name = input("Enter directory name to delete: ").strip()
                    try:
                        self.delete_directory(dir_name)
                    except FileNotFoundError as e:
                        print(e)
                case "3":
                    try:
                        self.list_directory_content()
                    except FileNotFoundError as e:
                        print(e)
                case "4":
                    dir_name = input("Enter directory name: ").strip()
                    try:
                        self.change_directory(dir_name)
                    except FileNotFoundError as e:
                        print(e)
                case "5":
                    return
                case _:
                    print("Invalid input. Please enter a valid choice.")


if __name__ == "__main__":
    builder = DirectoryBuilder()
    builder.start()