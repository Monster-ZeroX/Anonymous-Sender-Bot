from pyrogram import (
    Client,
    filters
    )
from database.userchats import add_chat
from database.blacklist import check_blacklist


@Client.on_message(filters.group)
async def copymes(client, message):
    fromuser = message.from_user.id
    if check_blacklist(fromuser):
      return
    add_chat(fromuser)
    await message.copy(message.chat.id,caption="")
