import csv
import io

def read_csv_lines(filename, bucket):
    # Get a handle on the object used in the run
    obj = bucket.Object(key = filename)

    # Get the object
    response = obj.get()
    
    # Read the contents of the file and split it into a list of lines
    lines = response['Body'].read().decode('utf-8')
    lines = list(csv.reader(io.StringIO(lines), delimiter=','))
    
    return lines