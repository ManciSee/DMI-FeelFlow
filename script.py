from telethon.sync import TelegramClient
import datetime
import pandas as pd
import json

# 1) .env is not configured
# 2) the script make a json file
# 3) in chats goes the telegram ID of the username.

api_id = "" # INSERT ID 
api_hash ="" # INSERT HASH 
chats = ['mancisee']

# Create a TelegramClient instance
client = TelegramClient('test', api_id, api_hash)

# Ensure that the client connection is properly closed
try:
    client.start()
    data_list = []
    for chat in chats:
        for message in client.iter_messages(chat, offset_date=datetime.date.today(), reverse=True):
            print(message)
            data = {"group": chat, "sender": message.sender_id, "text": message.text, "date": str(message.date)}
            data_list.append(data)

finally:
    client.disconnect()

# Save the data_list to a JSON file
output_file_path = "messages_data_{}.json".format(datetime.date.today())
with open(output_file_path, 'w') as f:
    json.dump(data_list, f, indent=4)

print(f"Messages data saved to {output_file_path}")
