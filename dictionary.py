city_map = {}  # city_map = dict()

city_map["Canada"] = []

cities = ["Calgary", "Toronto", "Vancouver"]
city_map["Canada"] +=  cities
print(city_map)

city_map["Canada"].append(cities)
print(city_map)

city_map["Canada"] +=  cities
print(city_map)

print(city_map.values())

print(city_map.keys())

print(city_map.items())
city_map.