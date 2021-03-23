import json
from urllib.request import urlopen

from transform_world import add_individual_kering


def load_world_data(conn, countries_list):

    url_link = "https://kering-group.opendatasoft.com/api/records/1.0/search/?dataset=epl-agregated-valued-results-2019&q=&rows=6800&facet=raw_material_group&facet=tier&facet=year&facet=raw_material_ods&facet=business_unit_ods&facet=process_step_ods&facet=impact_contry_ods&facet=environmental_impact_group_ods&refine.year={year}&refine.impact_contry_ods={country}"

    years = [2018, 2019]
    sql = """INSERT INTO World_Emissions (record_id, impact_country,
                         raw_material, valued_result, tier, business_unit,
                         year, raw_material_group, process_step, environmental_impact_group)
                         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor = conn.cursor()

    total = 0
    for current_year in years:
        for current_country in countries_list:

            insert_list = []

            current_country = current_country.replace(" ", "+")
            with urlopen(url_link.format(year=int(current_year), country=str(current_country))) as response:
                source = response.read()
            data = json.loads(source)
            for record in data['records']:
                val = list(add_individual_kering(record))
                insert_list.append(val)
            total += len(insert_list)

            cursor.executemany(sql, insert_list)
            conn.commit()
            text = " for {country} in {year}".format(country=current_country, year=current_year)
            print("Submitted " + str(len(insert_list)) + text)

    cursor.executemany(sql, insert_list)
    conn.commit()
    print('')
    print("Submitted " + str(total))
    cursor.close()
