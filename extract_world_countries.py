import json
from urllib.request import urlopen


def get_countries_list():
    url_link = "https://kering-group.opendatasoft.com/api/records/1.0/search/?dataset=epl-agregated-valued-results-2019&q=&facet=raw_material_group&facet=tier&facet=year&facet=raw_material_ods&facet=business_unit_ods&facet=process_step_ods&facet=impact_contry_ods&facet=environmental_impact_group_ods"
    with urlopen(url_link) as response:
        source = response.read()

    data = json.loads(source)

    countries_list = []

    for i in range(len(data['facet_groups'][0]['facets'])):
        countries_list.append(data['facet_groups'][0]['facets'][i]['name'])


###################################################################################################################
    second_url = url_link
    for country_name in countries_list[:-2]:
        country_name = country_name.replace(" ", "+")
        string_to_add = "&exclude.impact_contry_ods={country_name_to_remove}".format(country_name_to_remove=country_name)
        second_url += string_to_add

    with urlopen(second_url) as response:
        source = response.read()

    data = json.loads(source)

    for i in range(len(data['facet_groups'][0]['facets'])):
        countries_list.append(data['facet_groups'][0]['facets'][i]['name'])

    countries_list = set(countries_list)
    countries_list = list(countries_list)
    countries_list.sort()

    # for country in countries_list:
    #     print(country)
    print('Found ' + str(len(countries_list)) + ' countries.')

    return countries_list
