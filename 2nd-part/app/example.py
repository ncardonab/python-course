import country

# print(country.data)
# country.run()

print("File 2 __name__ = %s" % __name__)

if __name__ == "__main__":
    print(f"File {__name__} is being run directly")
else:
    print(f"File {__name__} is being imported")
