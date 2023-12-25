import csv

world_population = 8064064330

# Did before knowing how it works


def read_csv_dumb_way(path):
    with open(path, 'r', encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        headers = next(reader)

        countries_data = []
        for line in reader:
            item = {}
            for index, header in enumerate(headers):
                print(header)
                item[header] = line[index]

            item['World Population Percentage'] = round(
                int(item['2022 Population']) / world_population, 3)
            countries_data.append(item)

        return countries_data

# Right after learning zip


def read_csv(path):
    with open(path, 'r', encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        headers = next(reader)

        countries_data = []
        for line in reader:
            iterable = zip(headers, line)
            country_dictionary = {key: value for key, value in iterable}
            countries_data.append(country_dictionary)

        return countries_data
