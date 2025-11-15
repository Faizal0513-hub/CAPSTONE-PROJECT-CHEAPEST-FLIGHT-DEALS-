class FlightData:
   
    def __init__(self,price,departure_code,arrival_code,departure_date,return_date):
        self.price =price
        self.departure_code = departure_code
        self.arrival= arrival_code
        self.departure_date= departure_date
        self.return_date = return_date


def find_cheapest_flights(data):
  

   
    if data is None or not data['data']:
       print("No flight data")
       return FlightData("N/A","N/A","N/A","N/A","N/A")
       
    first_flight= data["data"][0]
    lowest_price= float(first_flight["price"]["grandTotal"])
    departure_code= first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    arrival_code= first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    departure_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date= first_flight["itineraries"][0]["segments"][0]["arrival"]["at"].split("T")[0]


    cheapest_flights = FlightData(lowest_price,departure_code,arrival_code,departure_date,return_date)
    
    for flight in data['data']:
        price=float(first_flight["price"]["grandTotal"])
        if price < lowest_price:
            departure_code = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            arrival_code = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            departure_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][0]["segments"][0]["arrival"]["at"].split("T")[0]
            cheapest_flights = FlightData(lowest_price, departure_code, arrival_code, departure_date, return_date)
            print(f"The Lowest Price to the {departure_code} is {lowest_price}")
    return cheapest_flights
    
                
   
       
       
   
