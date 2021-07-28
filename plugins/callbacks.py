from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.setting import caption_False, caption_True

from .start import REPLY_MARKUP, START


@Client.on_callback_query(filters.regex("^captz$"))
async def capa(_, query):
    await query.edit_message_text(
        "Do You Need Caption for Media Messages ?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Yes ✅", callback_data="ca_yes"),
                    InlineKeyboardButton(text="No ❌", callback_data="ca_no"),
                ],
                [InlineKeyboardButton(text="Back", callback_data="bbb")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("^ca_yes$"))
async def captyes(_, query):
    caption_True(query.from_user.id)
    await query.edit_message_text(
        "Auto Caption Setting - `True`",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Back", callback_data="bbb")]]
        ),
    )


@Client.on_callback_query(filters.regex("^ca_no$"))
async def captno(_, query):
    caption_False(query.from_user.id)
    await query.edit_message_text(
        "Now, You will Get No Captions !",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Back", callback_data="bbb")]]
        ),
    )


@Client.on_callback_query(filters.regex("^bbb$"))
async def backbtt(_, query):
    await query.edit_message_text(
        START, reply_markup=REPLY_MARKUP, disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("^(yes|no)-"))
async def cbb(client, call):
    k = call.data
    msgid = int(k.split("-")[1])
    chat = call.message.chat.id
    if k.startswith("yes"):
        await call.message.delete()
        await call.message._client.copy_message(chat, chat, msgid)
    if k.startswith("no"):
        await call.message.delete()
        await call.message._client.copy_message(chat, chat, msgid, caption="")
