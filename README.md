# Telegram attachment downloader
Download all previous attachments in chat or monitor/download new uploads
Uses a 'user' bot since regular bots cannot monitor chats unless they are a group admin.

## Setup
#### 1. Register a Telegram App:
```
https://my.telegram.org/apps
```


#### 2. Take the API_ID, API_HASH and the channel URL and replace in the script. 
```
API_ID = 11111111
API_HASH = 'abcdefghijklmnopq123456789000000'
CHAT_URL = 'https://t.me/+restofthechaturl'
```

#### 3. Run the script once in 'monitor' mode.
When you run the script for a chat/group for the first time, it will prompt for phonenumber and a token you will receive on this number.
After this a session will get established, which can be named by changing the `SESSION_NAME` variable.
```
(venv)user@debian:~/$ python main.py monitor
Starting monitor, waiting for new messages

Please enter your phone (or bot token): +3188888888
Please enter the code you received: 13337
```
