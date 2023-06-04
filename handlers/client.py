from telethon import TelegramClient 


api_id = 10738943
api_hash = 'da61e3a08b5ac78ce28b4a4cd854aeec'
news_api = '6ee5a3c2aa074546bc12b1e05a1da1e2'

# with TelegramClient(StringSession(), api_id, api_hash) as client:
#     session_str

client = TelegramClient('session', api_id , api_hash)
