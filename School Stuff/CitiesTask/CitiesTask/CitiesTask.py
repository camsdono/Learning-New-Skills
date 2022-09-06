class Place():
    def __init__(self):
        self.city = ""
        self.country = ""
        self.population = ""
        self.language = ""

places = [Place() for x in range(3)]



for x in range(len(places)):
    places[x].city = str(input("Enter city name: "))
    places[x].country = str(input("Enter cities country: "))
    places[x].population = float(input("Enter population: "))
    places[x].language = str(input("Enter countries language: "))
    print("")

def displayData():
    for x in range(len(places)):
        print(places[x].city)
        print(places[x].country)
        print(places[x].population)
        print(places[x].language)
        print("")

displayData()