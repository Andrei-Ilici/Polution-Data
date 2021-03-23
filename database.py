import os
import pymysql


# Use pymysql Python module to connect to the RDS MySQL database on Amazon Web Services.
def connect_to_db():
    conn = pymysql.connect(
        host=os.environ.get('MY_SQL_HOST'),
        port=int(os.environ.get('MY_SQL_PORT')),
        user=os.environ.get('MY_SQL_USER'),
        passwd=os.environ.get('MY_SQL_PASSWORD'),
        charset='utf8mb4')
    
    print("Successfully connected to the database.")
    return conn


# Create the database to be used
def create_database(conn):
    create_database_sql = '''create database IF NOT EXISTS Project'''
    cursor = conn.cursor()
    cursor.execute(create_database_sql)
    conn.commit()
    cursor.close()
    print("Successfully created Project database.")


# Select the database to be used
def use_database(conn):
    use_database_sql = '''use Project'''
    cursor = conn.cursor()
    cursor.execute(use_database_sql)
    conn.commit()
    cursor.close()
    print("Selected Project database.")


# Create first table in the database
# Save the UK Emissions data here
def create_uk_table(conn):
    create_table1_sql = ''' CREATE TABLE IF NOT EXISTS UK_Emissions(
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

    cursor = conn.cursor()
    cursor.execute(create_table1_sql)
    conn.commit()
    cursor.close()
    print("Successfully created UK Table.")


# Create second table in the database
# Save the World Emissions coming from the Kering API here
def create_world_table(conn):

    create_table2_sql = """ CREATE TABLE IF NOT EXISTS World_Emissions(
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

    cursor = conn.cursor()
    cursor.execute(create_table2_sql)
    conn.commit()
    cursor.close()
    print("Successfully created World Table.")
