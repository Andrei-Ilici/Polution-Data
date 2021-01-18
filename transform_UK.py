
def individual_data_insertion(category,current_big_list,i):
    measure = category
    year = current_big_list[i][0]
    quarter = current_big_list[i][1]
    energy_supply = current_big_list[i][2]
    bussiness = current_big_list[i][3]
    transport = current_big_list[i][4]
    public = current_big_list[i][5]
    residential = current_big_list[i][6]
    other_sectors = current_big_list[i][7]
    total_co2 = current_big_list[i][8]
    other_gases = current_big_list[i][9]
    other_gas_emissions = current_big_list[i][10]
    val = (measure, year, quarter, energy_supply, bussiness, transport, public, residential, other_sectors, total_co2, other_gases, other_gas_emissions)
    return val