#Read the contents of a text file from disk, Make an edit and save it as a new name

file_path = ("D:\Github\Nackademin-Python\smereka.txt")

def read_file (file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return None

def write_file (file_path, content):
        return content