# from telethon import TelegramClient, sync

# # Replace these values with your own
# api_id = 21014514
# api_hash = '4493b4a38e7b95a3f05fcf1f5d2cb03d'
# phone_number = '+393885845333'
# chat_id = 'Spotted_DMI'
# message_id = 16116

# # Create a Telegram client
# with TelegramClient('session_name', api_id, api_hash) as client:
#     # Use the entity of the group chat you want to retrieve messages from
#     entity = client.get_entity(chat_id)

#     # Use the get_messages method to retrieve messages from the group
#     messages = client.get_messages(entity, limit=10)  # You can specify the number of messages to retrieve

#     # Print the retrieved messages
#     for message in messages:
#         print(message.text)
# # Create an empty list to store the comments
#     comments = []

# # Iterate over the retrieved messages and add any comments to the list
#     for message in messages:
#         if message.reply_to_msg_id == message_id:
#             comments.append(message)
            
#         print("------------------- PRINT 2°  -----------------")
#         print(comments)

# # Print the comments
#     print("-------------------- COMMENTI ------------------ ")
#     for comment in comments:
#         print(comment.text)
