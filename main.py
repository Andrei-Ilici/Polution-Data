import os
import io
import pymysql
import pandas as pd
import boto3
import csv
# import requests
import json
from urllib.request import urlopen

from bucket import connect_to_s3, list_s3_objects
from database import connect_to_db, create_database, use_database, create_uk_table, create_world_table

from extract_world_countries import get_countries_list
from extract_UK import read_csv_lines, create_single_list, create_complete_list
from transform_UK import individual_data_insertion
from load_UK import insert_data_to_database

# from extract_world import
from transform_world import add_individual_kering
from load_world import load_world_data

# Firstly connect to the database and create the required tables
conn = connect_to_db()
cursor = conn.cursor()
print('\n')

try:
    create_database(conn)
except Exception as ERROR:
    print('Error when creating database: ' + str(ERROR))

try:
    use_database(conn)
except Exception as ERROR:
    print('Error when selecting database: ' + str(ERROR))
print('')

try:
    create_uk_table(conn)
except Exception as ERROR:
    print('Error when creating UK table: ' + str(ERROR))

try:
    create_world_table(conn)
except Exception as ERROR:
    print('Error when creating World table: ' + str(ERROR))
print('')

# Now it's time to read the files in S3 and process the UK data
bucket_name = os.getenv('AWS_BUCKET_NAME')
try:
    s3 = connect_to_s3()
except Exception as ERROR:
    print('Error when connecting to Amazon S3: ' + str(ERROR))

try:
    list_s3_objects(s3, bucket_name)
except Exception as ERROR:
    print('Error when reading files from the S3 bucket: ' + str(ERROR))
print('')

# Process UK data through ETL

file_list = ("Table1.csv", "Table2.csv", "Table3.csv", "Table4.csv")
for filename in file_list:
    try:
        lines = read_csv_lines(filename, bucket_name, s3)
        big_list = create_complete_list(filename, lines)
        category = lines[0][1]
        insert_data_to_database(conn, big_list, category, lines)
    except Exception as ERROR:
        print('Error when processing UK data: ' + str(ERROR))
print('')

# Process World data coming from the Kering API

try:
    countries_list = get_countries_list()
except Exception as ERROR:
    print('Error when extracting list of countries: ' + str(ERROR))
print('')

try:
    load_world_data(conn, countries_list)
except Exception as ERROR:
    print('Error when loading world data: ' + str(ERROR))
print('')
