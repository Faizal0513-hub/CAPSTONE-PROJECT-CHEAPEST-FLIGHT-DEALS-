from datetime import datetime
import os
import requests
from dotenv import load_dotenv



load_dotenv()
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_ENDPOINT= "https://test.api.amadeus.com/v1/reference-data/locations/cities"
CHEAP_FLIGHTS_ENDPOINT="https://test.api.amadeus.com/v1/shopping/flight-destinations"


class FlightSearch:
    
    
    def __init__(self):
        self._api_key=os.environ["AMADEUS_API_KEY"]
        self.api_secret = os.environ["AMADEUS_API_SECRET"]
        self._token =  self._get_new_token()
        
    
    def get_destination(self,city_name):
    
        headers ={"Authorization" : f"Bearer {self._token}"
          }
          
        
        query = {
                "keyword": city_name,
                "subType": "CITY,AIRPORT",
                "max": 2
        }
        response =requests.get(AMADEUS_ENDPOINT,headers=headers,params=query)
        print(f"Status Code {response.status_code}  Airport IATA {response.text}")
        
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError : no airport code found for {city_name}")
            return "N/A"
            
        except KeyError:
            print(f"KeyError : no airport code found for {city_name}")
            return "Not Found"
            
        return code
    
    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id':  self._api_key,
            'client_secret':  self.api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT,headers=header,data=body)
        print(f"your token is {response.json()['access_token']}")
        print(f"your token is {response.json()['expires_in']} seconds")
        return response.json()['access_token']
    
    
    def check_flights(self,origin_code,destination_code,departure_date,return_date):
        header = {"Authorization": f"Bearer {self._token}  "
                  
                  }
        
        parameter = {"originLocationCode": origin_code,
                     "destinationLocationCode": destination_code,
                     "departureDate": departure_date.strftime("%Y-%m-%d"),
                     "returnDate" : return_date.strftime("%Y-%m-%d"),
                     "adults": 1,
                     "nonStop": "false",
                     "currencyCode": "GBP",
                     "max": "250"
                     }
        
        response = requests.get(url=CHEAP_FLIGHTS_ENDPOINT, headers=header, params=parameter)
        print(response.raise_for_status())
        data = response.json()
        print(data)
        
        if response.status_code!=200:
            print(f"check_flights() response code : {response.status_code}")
            print(f"Response Body : {response.text}")
            return None
        
        return response.json()
    
    
   