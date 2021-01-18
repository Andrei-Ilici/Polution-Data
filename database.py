import os
import pymysql

def connect_to_db():
    conn = pymysql.connect(
        host = os.environ.get('MY_SQL_HOST'),
        port = int(os.environ.get('MY_SQL_PORT')),
        user = os.environ.get('MY_SQL_USER'),
        passwd = os.environ.get('MY_SQL_PASSWORD'),
        charset='utf8mb4')

    # cursor = conn.cursor()
    return conn

def print_vers(cursor):
    cursor.execute("select version()")

def create_database():
    create_database_sql = '''create database Project'''
    cursor.execute(create_database_sql)
    conn.commit()

def use_database():
    use_database_sql = '''use Project'''
    cursor.execute(use_database_sql)
    conn.commit()

def create_uk_table():
    create_table1_sql = ''' CREATE TABLE UK_Emissions(
    measure VARCHAR(100) NOT NULL,
    year INT(4) NOT NULL,
    quarter CHAR(2) NOT NULL,
    energy_supply FLOAT NOT NULL,
    bussiness FLOAT NOT NULL,
    transport FLOAT NOT NULL,
    public FLOAT NOT NULL,
    residential FLOAT NOT NULL,
    other_sectors FLOAT NOT NULL,
    total_co2 FLOAT NOT NULL,
    other_gases FLOAT NOT NULL,
    other_gas_emissions FLOAT NOT NULL
    )'''
    
    cursor.execute(create_table1_sql)
    conn.commit()

def create_world_table():
    
    create_table2_sql = """ CREATE TABLE World_Emissions(
    record_id VARCHAR(50) NOT NULL,
    impact_country VARCHAR(50) NOT NULL,
    raw_material VARCHAR(50) NOT NULL,
    valued_result FLOAT NOT NULL,
    tier INT(2),
    business_unit VARCHAR(50) NOT NULL,
    year INT(4),
    raw_material_group VARCHAR(50) NOT NULL,
    process_step VARCHAR(50) NOT NULL,
    environmental_impact_group VARCHAR(50) NOT NULL
    )"""

    cursor.execute(create_table2_sql)
    conn.commit()