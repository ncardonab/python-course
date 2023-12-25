import utils 

keys, values = utils.get_population()

data = [
    {
        "name": "Qatar",
        "population": 2881060,
        "gdp": 334524,
        "employability": "high"
    },
    {
        "name": "Luxembourg",
        "population": 590667,
        "gdp": 118200,
        "employability": "high"
    },
    {
        "name": "Singapore",
        "population": 5703600,
        "gdp": 372063,
        "employability": "high"
    },
    {
        "name": "Brunei",
        "population": 428697,
        "gdp": 114160,
        "employability": "high"
    },
    {
        "name": "Ireland",
        "population": 4937786,
        "gdp": 388877,
        "employability": "high"
    },
    {
        "name": "Norway",
        "population": 5367580,
        "gdp": 403287,
        "employability": "high"
    },
    {
        "name": "United Arab Emirates",
        "population": 9856000,
        "gdp": 421144,
        "employability": "high"
    },
    {
        "name": "Kuwait",
        "population": 4420110,
        "gdp": 288432,
        "employability": "high"
    },
    {
        "name": "Switzerland",
        "population": 8544034,
        "gdp": 707115,
        "employability": "high"
    },
    {
        "name": "United States",
        "population": 331002651,
        "gdp": 21439453,
        "employability": "high"
    }
]

def run():
    print ("File 1 __name__ = %s" %__name__) 
    # country_name = input('Enter the country name: ')
    # country_info = utils.population_by_country(data, country_name)[0]

    # print("Country name:", country_info['name'])
    # print("Population:", country_info['population'])
    # print("GDP:", country_info['gdp'])
    # print("Employability:", country_info['employability'])

if __name__ == "__main__":
    print(f"File {__name__} is being run directly")
    run()
else:
    print(f"File {__name__} is being imported")
    run()