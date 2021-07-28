from pyrogram import Client, filters

from database.blacklist import add_blacklist, get_blacklisted, remove_blacklist
from vars import var


@Client.on_message(filters.command("black") & filters.user(int(var.OWNER_ID)))
async def black_user(_, message):
    try:
        bl = int(message.text.split(" ", maxsplit=1)[1])
    except IndexError:
        return await message.reply_text("Whom to Blacklist ?")
    add_blacklist(bl)
    await message.reply_text(f"Blacklisted {bl} !")


@Client.on_message(filters.command("unblack") & filters.user(int(var.OWNER_ID)))
async def unblack_user(_, message):
    try:
        bl = int(message.text.split(" ", maxsplit=1)[1])
    except IndexError:
        return await message.reply_text("Whom to Blacklist ?")
    te = remove_blacklist(bl)
    await message.reply_text(te)


@Client.on_message(filters.command("listblack") & filters.user(int(var.OWNER_ID)))
async def liblack(_, message):
    m = await message.reply_text("`...`")
    al = get_blacklisted()
    TE = "List of Blacklisted User !"
    for on in al:
        TE += "\n" + str(on)
    await m.edit_text(TE)
