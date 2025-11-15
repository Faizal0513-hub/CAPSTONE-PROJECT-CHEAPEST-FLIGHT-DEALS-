from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flights
from notification_manager import NotificationManager
from datetime import timedelta,datetime
import time

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager

ORIGIN_CITY_IATA = "PAR"

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination(row["city"])
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data=sheet_data
data_manager.update_destination_code()


tomorrow  =  datetime.now() + timedelta(days=1)
six_month_after = datetime.now() + timedelta(days=(6*30))

for destination in  sheet_data:
    print(f"Getting flights for{ destination}")
    flights = flight_search.check_flights(ORIGIN_CITY_IATA,
                                          destination["iataCode"],
                                          from_time=tomorrow,
                                          to_time=six_month_after,
                                          )
    
    cheapest_flight = find_cheapest_flights(flights)
    if cheapest_flight.price != "N/A" and cheapest_flight.price <  destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['City']}")
        notification_manager.send_notification(message_body=f"Low Price alert! Only € {cheapest_flight.price} to fly from {cheapest_flight.departure_code} to {cheapest_flight.arrival_code} on {cheapest_flight.departure_date}  until {cheapest_flight.return_date} " )


