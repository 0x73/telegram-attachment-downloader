from telethon import TelegramClient, events
import os
import argparse
import asyncio

# Set required variables
API_ID = <API_ID>
API_HASH = '<APIHASH>'
CHAT_URL = '<CHAT_URL>'
SESSION_NAME = 'my_session'

# initialize the client
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

@client.on(events.NewMessage(chats=[CHAT_URL])) 

# Handle message
async def process_message(message):
    if message.file and message.file.name and os.path.exists(os.path.join("./attachments", message.file.name)):
        print(f"File {message.file.name} already exists, skipping download\n")
    elif message.file and message.file.name is None:
        print(f"Media type does not store original filename")
        filename = await message.download_media(file="./attachments/")
        print(f"Downloaded media: {filename}\n")
    elif message.file:
        attachment = await message.download_media(file="./attachments/")
        print(f"Downloaded file: {attachment}\n")

# Process previous messages that include media
async def process_history():
    print("Processing all messages in chat history...")
    async for message in client.iter_messages(CHAT_URL):
        if message.media:
            await process_message(message)
    print("Finished processing chat history.")

async def run_client(mode):
    if mode == 'history':
        print(f"Starting {mode}, processing previous messages\n")
        await client.connect()
        await process_history()
    if mode == 'monitor':
        print(f"Starting {mode}, waiting for new messages\n")
        await client.start()
        await client.run_until_disconnected()
    else:
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor for new Telegram messages containing attachments in a chat or download attachments from all previous messages in a chat.") 
    parser.add_argument('mode',choices=["monitor","history"],help=("Specify the operation mode. "
                                                                   "'monitor' starts monitoring for new messages, "
                                                                   "while 'history' downloads attachments from previous messages. "),)
    args = parser.parse_args()
    asyncio.run(run_client(args.mode))
