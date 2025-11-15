from twilio.rest import Client
import os
from dotenv import load_dotenv
ACCOUNT_SID= os.environ["ACCOUNT_SID"]
AUTH_TOKEN= os.environ["AUTH_TOKEN"]
load_dotenv()


class NotificationManager:
    def __init__ (self):
        self.client = Client(ACCOUNT_SID,AUTH_TOKEN)

        
        
        
        
    def send_notification(self,message_body):
           
             
            message = self.client.messages.create(
                from_= os.environ["TWILIO_NUMBER"],
                body= message_body,
                to = os.environ["WHATSAPP_NUMBER"],
            
            )
            
            print(message.status)
        

