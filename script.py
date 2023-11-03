from pyrogram import Client
from datetime import datetime
import json
import time

# Replace these values with your own
api_id = 21014514
api_hash = '4493b4a38e7b95a3f05fcf1f5d2cb03d'
channel_id = 'Spotted_DMI'

# Create a Pyrogram client
app = Client('session_name', api_id=api_id, api_hash=api_hash)
started = datetime.today()

print("app started successfully")
app.start()
i = 0
json_data = {}

for message in app.get_chat_history('Spotted_DMI', limit=100, offset_date=datetime.today()):
    i += 1
    print("\n##### Spot numero: " + str(i) + " ID : " + str(message.id))
    print(message.text
          )
    data = {
        "Spot": message.text,
        "Comments": []
    }
    print("\n#### Commenti del post con ID :" + str(message.id))
    for reply in app.get_discussion_replies('Spotted_DMI', message.id):
        print(reply.text)
        data["Comments"].append(reply.text)
        time.sleep(2)
    json_data[message.id] = data

with open("data.json", "w") as json_file:
    json.dump(json_data, json_file, indent=4, ensure_ascii=False)

app.stop()
