from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
from pyrogram.enums import ChatType
from pyrogram.errors import UserNotParticipant
from YousefMusic import app
import config

channel = config.YAFA_CHANNEL
Nem = config.BOT_NAME + " شغل"
async def subscription(_, __: Client, message: Message):
    user_id = message.from_user.id
    try: 
        await app.get_chat_member(channel, user_id)
    except UserNotParticipant: 
        return False
    return True
    
subscribed = filters.create(subscription)

# تعريف دالة لمعالجة الأوامر
@app.on_message(filters.command(["تشغيل", "شغل",Nem],"") & ~subscribed)
async def command_handler(_: Client, message: Message):
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        user_id = message.from_user.id
        user = message.from_user.first_name
        markup = Markup([
            [Button(config.YAFA_NAME, url=f"https://t.me/{channel}")]
        ])
        await message.reply(
            f"◇ عذرًا عزيزي {user} ، عليك الاشتراك في قناة البوت أولاً.",
            reply_markup=markup
        )
        
