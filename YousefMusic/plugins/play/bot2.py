import asyncio
import random
from pyrogram import enums
from pyrogram import types
from YousefMusic.misc import SUDOERS
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from YousefMusic import app
from config import *

bot_name = {}

name = "بلاك"

@app.on_message(filters.regex("تعيين اسم البوت")& filters.private & SUDOERS, group=7113)
async def set_bot_name(client, message):
    global name
    ask = await app.ask(message.chat.id, "ارسل الاسم الجديد", timeout=300)
    name = ask.text
    await message.reply_text("تم تعيين الاسم بنجاح")

Mazen_responses = [
    "تئبرني 😂♥️ ،",
    "قلب لينو 🥹💘 ⋅",
    "نعم يا عيوني 💘 ،",
    "روح لينو",
    "ايه يا معلم مين مزعلك",
    "ايوه جايه 😂♥️،",
    "تًبا لك يا وجه البرص 🙂",
]

@app.on_message(filters.command(["بلاكي", "بلاك"], ""), group=71135)
async def Mazen_bot(client, message):
    global name
    bot_username = (await app.get_me()).username
    bar = random.choice(Mazen_responses).format(name=name)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("خدني لجروبك 🫣♥", url=f"https://t.me/{bot_username}?startgroup=True")]
    ])
    
    await message.reply_text(
        text=f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**",
        disable_web_page_preview=True,
        reply_markup=keyboard,
    parse_mode=enums.ParseMode.MARKDOWN)
