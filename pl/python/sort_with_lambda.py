cities = ["arta", "ioannina", "preveza", "Igoumenitsa"]

cities.sort(key=lambda a: len(a))
for city in cities:
    print(city)
