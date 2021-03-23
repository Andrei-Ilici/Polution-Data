import csv
import io


def read_csv_lines(filename, bucketname, s3):
    bucket = s3.Bucket(bucketname)
    # Get a handle on the object used in the run
    obj = bucket.Object(key=filename)

    # Get the object
    response = obj.get()

    # Read the contents of the CSV file and split it into a list of lines
    lines = response['Body'].read().decode('utf-8')
    lines = list(csv.reader(io.StringIO(lines), delimiter=','))

    return lines


def create_single_list(elem, number):
    current_list = []

    for i in range(1, len(elem)):
        current_list.append(elem[i][number])

    return current_list


def create_complete_list(filename, lines):
    big_list = []

    for j in range(len(lines[2])):
        big_list.append(create_single_list(lines, j))

    return big_list
