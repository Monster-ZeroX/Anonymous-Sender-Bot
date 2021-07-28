import logging

from pyrogram import Client, idle

from vars import var

logging.getLogger("pyrogram").setLevel(logging.INFO)

AnonyBot = Client(
    "Anonymous-Sender",
    api_id=var.API_ID,
    api_hash=var.API_HASH,
    bot_token=var.BOT_TOKEN,
    plugins=dict(root="plugins"),
)

AnonyBot.start()
uname = (AnonyBot.get_me()).username
print(f"@{uname} Deployed Successfully !")

idle()
