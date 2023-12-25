#!/usr/bin/env python3

""" utils.py - module that provides functions to handle world population data"""

import re
def get_population() -> tuple:
    keys = ['col', 'bol']
    values = [300, 400]
    return keys, values


def get_population_by_year(world_population):
    population_by_year = {}
    for country_data in world_population:
        for key, value in country_data.items():
            year_key = key.split(' ')[0]
            if re.search(r"\d{4}", year_key):
                population_by_year[year_key] = int(value)
    return population_by_year


def most_populated_country(world_population):
    return max(world_population, key=lambda country: country["2022 Population"])


def get_population_by_country(data, country_name):
    country_values = list(
        filter(lambda country: country['name'] == country_name, data))
    return country_values


def display_country_data(country):
    for key, value in country.items():
        print(f'{key}: {value}')

def get_column(world_population, column_name):
    country_names, column_values = zip(*list(map(lambda country: ( country["Country/Territory"], country[column_name] ), world_population)) )
    return country_names, column_values