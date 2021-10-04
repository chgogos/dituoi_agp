cities = ["arta", "ioannina", "preveza", "igoumenitsa"]
cities.sort(key=lambda a: len(a))

for city in cities:
    print(city)
