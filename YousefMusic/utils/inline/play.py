import math

from YousefMusic import app 

from pyrogram.types import InlineKeyboardButton

from YousefMusic.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)

    buttons = [
                [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],[  
            InlineKeyboardButton(text="انهاء", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="استكمال", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="ايقاف", callback_data=f"ADMIN Pause|{chat_id}"),
            
        ],[
            InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋 ", url=f"https://t.me/cecrr"),
            
        ],[
            InlineKeyboardButton(text="- 𝙔𝙤𝙪𝙨𝙚𝙛", url=f"https://t.me/y_o_v"),
        ],[
            InlineKeyboardButton(text="اضف البوت الي مجموعتك او قناتك⚡", url=f"https://t.me/{app.username}?startgroup=true")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="انهاء", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="استكمال", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="ايقاف", callback_data=f"ADMIN Pause|{chat_id}"),
            
        ],[
            InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋 ", url=f"https://t.me/cecrr"),
           
        ],[
            InlineKeyboardButton(text="- 𝙔𝙤𝙪𝙨𝙚𝙛", url=f"https://t.me/y_o_v"),
        ],[
            InlineKeyboardButton(text="⚡اضف البوت الي مجموعتك او قناتك", url=f"https://t.me/{app.username}?startgroup=true")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"ModyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"ModyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="𝐑𝐄𝐒𝐔𝐌𝐄",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
