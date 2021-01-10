import os

def get_file_path(filename):
    d = os.getcwd()
    relative_path = r"app/data/" + filename + ".csv"
    file_path = os.path.join(d, relative_path)
    
    return file_path
