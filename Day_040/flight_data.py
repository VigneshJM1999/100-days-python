class FlightData:
    def __init__(self, data):
        self.price = data["price"]["total"]
        itinerary = data["itineraries"][0]["segments"]
        self.origin_city = itinerary[0]["departure"]["iataCode"]
        self.destination_city = itinerary[-1]["arrival"]["iataCode"]
        self.departure_date = itinerary[0]["departure"]["at"].split("T")[0]
        self.return_date = data["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
        self.stops = len(itinerary) - 1
