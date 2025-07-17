from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_data()

flight_search = FlightSearch()
notifier = NotificationManager()

for destination in sheet_data:
    destination_code = destination.get("iataCode")
    if not destination_code:
        destination_code = flight_search.get_city_code(destination["city"])
        destination["iataCode"] = destination_code
        data_manager.update_data(destination)

    flight_data = flight_search.get_flights(destination_code)
    cheapest_flight = flight_search.find_cheapest_flight(flight_data)

    if cheapest_flight and cheapest_flight["price"] < destination["lowestPrice"]:
        message = (
            f"Low price alert! Only £{cheapest_flight['price']} to fly from "
            f"{cheapest_flight['from']} to {cheapest_flight['to']}, "
            f"{cheapest_flight['out_date']} to {cheapest_flight['return_date']}."
        )
        notifier.send_sms(message)