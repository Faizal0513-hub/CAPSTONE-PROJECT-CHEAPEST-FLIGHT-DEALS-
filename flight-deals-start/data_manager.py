import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()



sheety_endpoint = "https://api.sheety.co/37a68f5db9debde732ff76732dc19718/flightDeals/prices"





class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user=os.environ["SHEETY_USERNAME"]
        self._password =os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(sheety_endpoint,auth=self._authorization)
        data = response.json()
        print(data)
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            update_endpoint = f"{sheety_endpoint}/{city['id']}"
            response = requests.put(update_endpoint , json=new_data, auth=self._authorization)
            print(response.text)
            
  
        
