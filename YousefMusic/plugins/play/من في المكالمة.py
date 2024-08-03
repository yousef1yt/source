from pyrogram import filters, Client
from AlexaMusic import app
import asyncio
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AlexaMusic.core.call import Alexa
from AlexaMusic.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)

@app.on_message(filters.regex("^مين في الكول$"))
async def strcall(client, message):
    assistant = await group_assistant(Alexa,message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("./Alexa/assets/call.mp3"), stream_type=StreamType().pulse_stream)
        text="الناس الكاعده تسولف :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يتكلم"
            else:
                mut="ساكت"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}➤{user.mention}➤{mut}\n"
        text += f"\nعددهم : {len(participants)}\n✔️"    
        await message.reply(f"{text}")
        await asyncio.sleep(7)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"المكالمه مغلقه الان")
    except TelegramServerError:
        await message.reply(f"قم بارسال الامر مره اخرى")
    except AlreadyJoinedError:
        text="الناس الي بتتكلم :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يتكلم"
            else:
                mut="ساكت"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}➤{user.mention}➤{mut}\n"
        text += f"\العدد : {len(participants)}\n✔️"    
        await message.reply(f"{text}")
