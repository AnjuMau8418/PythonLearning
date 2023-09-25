# Dictionary in List
travel_log = [
    {"country": "France",
     "cities": ["Paris", "Lille", "Dijon"],
     "visits": 12},
    {"country": "Germany",
     "cities": ["Berlin", "Hamburg", "Stuttgart"],
     "visits": 15},
]
country = input("Enter the country name: ")
total_visitors = int(input("Enter number of total visitor: "))
visited_cities = input("Enter the cities visited : ").split()


def add_new_country(country_visited, total_visitors_number, visited_cities_name):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities"] = visited_cities_name
    new_country["visits"] = total_visitors_number
    travel_log.append(new_country)


add_new_country(country, total_visitors, visited_cities)
print(travel_log)
