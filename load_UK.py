from transform_UK import individual_data_insertion

def insert_data_to_database(conn, big_list, category, lines):
    
    sql = "INSERT INTO UK_Emissions (measure, year, quarter, energy_supply, bussiness, transport, public, residential, other_sectors, total_co2, other_gases, other_gas_emissions) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
    cursor = conn.cursor()
    insert_list = []
    
    for j in range(1,len(lines[2])):
        val = list(individual_data_insertion(category, big_list, j))
        insert_list.append(val)
        
    cursor.executemany(sql, insert_list)
    
    conn.commit()
    cursor.close()

    print(str(cursor.rowcount) + " records inserted for " + str(category) + "." )
