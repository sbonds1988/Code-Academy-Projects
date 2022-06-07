destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]

attractions = []

for i in range(len(destinations)):
  attractions.append([])

def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions[destination_index] = attraction

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = test_traveler[1]
  for index in range(len(destinations)):
    if destinations[index] == traveler_destination:
      return index

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  possible_attraction = []
  attraction_tags = []
  for fun in attractions_in_city[0]:
    possible_attraction.append(fun)
  for tags in attractions_in_city[1]:
    attraction_tags.append(tags)
  for interest in interests:
    if attraction_tags.count(interest) > 0:
      attractions_with_interest.append(interest)
  return attractions_with_interest
    

  
#print(get_traveler_location(test_traveler))

test_destination_index = get_traveler_location(test_traveler)

add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["The Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site, monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions)

#la_arts = find_attractions("Los Angeles, USA", ["art"])
#print(la_arts)