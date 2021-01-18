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

print('problem is ')
print_vers(cursor)

s3 = connect_to_s3()
list_s3_objects(s3)
