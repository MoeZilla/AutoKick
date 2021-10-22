import os
from pyrogram import Client, filters, idle

API_ID = int(os.environ.get("API_ID", 1222))
API_HASH = os.environ.get("API_HASH")
TOKEN = os.environ.get("TOKEN")

app = Client(
    ':kick:',
    API_ID,
    API_HASH,
    bot_token=TOKEN,
)

@app.on_message(filters.command('start'))
def start(_,message):
    app.send_message(message.chat.id , "Hello I am AutoKick Bot") 

@app.on_message(filters.new_chat_members)
def kick(_,message):
   chat_id = message.chat.id
   user_id = message.from_user.id
        app.kick_chat_member(chat_id, user_id)
        app.unban_chat_member(chat_id, user_id)
        message.reply('Good Bye')

	
app.start()
idle()
