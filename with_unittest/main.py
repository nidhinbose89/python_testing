import os
import csv

def some_func(filename):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join( ROOT_DIR, filename)
    with open(file_path) as csv_file:
        reader_obj = csv.reader(csv_file)
        first_line_checked = False
        for row in reader_obj:
            if not first_line_checked and row[0] != '100':
                # finished first line check
                return {'message': 'first line error', 'status': False }
            first_line_checked = True
        if row[0] != '900':
            # last line check
            return {'message': 'last line error', 'status': False }
    return {'message': 'all ok', 'status': True }

if __name__ == "__main__":
    print(some_func(filename='input.csv'))
