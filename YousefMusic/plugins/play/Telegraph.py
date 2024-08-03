#https://t.me/Y_o_v
#_____@F_U_O

import os, asyncio
from typing import Optional
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from telegraph import upload_file
from YousefMusic import app




def get_file_id(msg: Message) -> Optional[Message]:
    if not msg.media:
        return None

    for message_type in ("photo", "animation", "audio", "document", "video", "video_note", "voice", "sticker"):
        obj = getattr(msg, message_type)
        if obj:
            setattr(obj, "message_type", message_type)
            return obj




@app.on_message(filters.command("ميديا", prefixes=""))
async def telegraph_upload(bot, update):
    replied = update.reply_to_message
    if not replied:
        return await update.reply_text("ريبلي على صورة أو مقطع فيديو أقل من 5 ميغابايت")
    file_info = get_file_id(replied)
    if not file_info:
        return await update.reply_text("Not Supported!")
    text = await update.reply_text(text="<code>التحميل على الخادم الخاص بي ...</code>", disable_web_page_preview=True)   
    media = await update.reply_to_message.download()   
    await text.edit_text(text="<code>اكتمل التنزيل. الآن أقوم بالتحميل على رابط تلكراف...</code>", disable_web_page_preview=True)                                            
    try:
        response = upload_file(media)
    except Exception as error:
        print(error)
        await text.edit_text(text=f"Error :- {error}", disable_web_page_preview=True)       
        return    
    try:
        os.remove(media)
    except Exception as error:
        print(error)
        return    
    await text.edit_text(
        text=f"<b>إليك رابط التلكراف الذي تم إنشاؤه  :-</b>\n\n<code>https://te.legra.ph{response[0]}</code>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(text="فتح الصوره", url=f"https://te.legra.ph{response[0]}"),
            InlineKeyboardButton(text="مشاركه", url=f"https://telegram.me/share/url?url=https://te.legra.ph{response[0]}")
            ],[
            InlineKeyboardButton(text="مسح", callback_data="close")
            ]])
        )
    
