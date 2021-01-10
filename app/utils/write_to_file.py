from utils.get_file_path import get_file_path
import csv
import traceback

def write_to_file(file_name, data):
    file_path = get_file_path(file_name)
    
    with open(file_path, "a", newline="") as file:

        mywriter = csv.writer(file)
        try:
            mywriter.writerow(data)

        except Exception as err:
            print(f"Couldn't print post: {data[0].name}")
            print(traceback.format_exc())
            print(err)
