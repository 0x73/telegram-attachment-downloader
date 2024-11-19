# Telegram attachment downloader
Telethon `User-bot` to download attachments in a specific Telegram channel/chat.
Can be used to:
  - Download all previous attachments in a chat
  - Monitor for new messages and download the attachments

Uses a 'user' bot since regular bots cannot monitor chats unless they are a group admin.

> "If cryptg is installed, the library will work a lot faster, since encryption and decryption will be made in C instead of Python." [docs](https://docs.telethon.dev/en/stable/basic/installation.html)

## Setup
#### 1. Install requirements
```
pip install -r requirements.txt
```

#### 2. Register a Telegram App:
Required to get `API_ID` and `API_HASH`
```
https://my.telegram.org/apps
```

#### 2. Replace the API_ID, API_HASH and the channel URL and replace in the script. 
Channel URL can be found in the `Channel Info` within the Telegram app
```
API_ID = 11111111
API_HASH = 'abcdefghijklmnopq123456789000000'
CHAT_URL = 'https://t.me/+restofthechaturl'
```

#### 3. Run the script once in 'monitor' mode.
When you run the script for a channel/chat for the first time, it will prompt for your phonenumber and a token you will receive on this number.
After this a session will get established, which can be named by changing the `SESSION_NAME` variable.
```
(venv)user@debian:~/$ python main.py monitor
Starting monitor, waiting for new messages

Please enter your phone (or bot token): +3188888888
Please enter the code you received: 13337
```
