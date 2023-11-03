from pyrogram import Client
import asyncio
from datetime import datetime

# Replace these values with your own
api_id = 21014514
api_hash = '4493b4a38e7b95a3f05fcf1f5d2cb03d'
channel_id = 'Spotted_DMI'


# Create a Pyrogram client
app = Client('session_name', api_id=api_id, api_hash=api_hash)
started = datetime.today()

print("app started succesfully ")
app.start()
for message in app.get_chat_history('Spotted_DMI',limit=2,offset_date=datetime.today()):
    print(message.text)
    
for message in app.get_discussion_replies('Spotted_DMI', 16116):
    print("--------- COMMENTI ---------------")
    print(message.text)
app.stop() 
