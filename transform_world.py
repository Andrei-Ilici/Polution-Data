

def add_individual_kering(record):
    record_id = record['recordid']
    impact_country = record['fields']['impact_contry_ods']
    raw_material = record['fields']['raw_material_ods']
    valued_result = record['fields']['valued_result']
    tier = record['fields']['tier']
    business_unit = record['fields']['business_unit_ods']
    year = record['fields']['year']
    raw_material_group = record['fields']['raw_material_group']
    process_step = record['fields']['process_step_ods']
    environmental_impact_group = record['fields']['environmental_impact_group_ods']
    val = (record_id, impact_country, raw_material, valued_result,
           tier, business_unit, year, raw_material_group,
           process_step, environmental_impact_group)
    return val
