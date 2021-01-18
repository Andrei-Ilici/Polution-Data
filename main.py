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
from database import print_vers, connect_to_db, create_database, use_database, create_uk_table, create_world_table

conn = connect_to_db()
cursor = conn.cursor()
print('')

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


bucket_name = os.getenv('AWS_BUCKET_NAME')
s3 = connect_to_s3()
list_s3_objects(s3, bucket_name)
