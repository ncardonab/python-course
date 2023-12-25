"""importing modules"""
import utils
from read_csv import read_csv
from chart import generate_bar_chart, generate_pie_chart

if __name__ == "__main__":
    world_population = read_csv('2nd-part/world_population.csv')
    max_country_population = utils.most_populated_country(world_population)
    utils.display_country_data(max_country_population)
    population_by_year = utils.get_population_by_year(world_population)

    labels = list(population_by_year.keys())
    values = list(population_by_year.values())
    # countries_by_continent = filter(lambda country: country["Continent"] == 'Europe', world_population)
    # country_names, percentages = utils.get_column(countries_by_continent, 'World Population Percentage')
    # # generate_bar_chart(labels, values)
    # # generate_bar_chart(country_names, percentages)
    # generate_pie_chart(country_names, percentages, 'World population percentages by Europe continent')

    