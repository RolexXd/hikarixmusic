import asyncio
import time
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import  config
from AloneMusic import app
from AloneMusic.misc import _boot_
from AloneMusic.plugins.sudo.sudoers import sudoers_list
from AloneMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from AloneMusic.utils.decorators.language import LanguageStart
from AloneMusic.utils.formatters import get_readable_time
from AloneMusic.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS, OWNER_ID
from strings import get_string


@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)

    loading_1 = await message.reply_text("💞")
    await asyncio.sleep(0.1)
    
    await loading_1.edit_text("<b>ʟᴏᴀᴅɪɴɢ</b>")
    await asyncio.sleep(0.1)
    await loading_1.edit_text("<b>ʟᴏᴀᴅɪɴɢ.</b>")
    await asyncio.sleep(0.1)
    await loading_1.edit_text("<b>ʟᴏᴀᴅɪɴɢ..</b>")
    await asyncio.sleep(0.1)
    await loading_1.edit_text("<b>ᴀʟᴍᴏsᴛ ʜᴇʀᴇ...</b>")
    await asyncio.sleep(0.1)
    await loading_1.delete()

    started_msg = await message.reply_text(text="<b>sᴛᴀʀᴛᴇᴅ...<a href='https://files.catbox.moe/xyy4qd.mp4' target='_blank'>ㅤ ㅤㅤㅤ</a></b>")
    await asyncio.sleep(0.4)
    await started_msg.delete()

    # Deep Linking Logic
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        
        if name.startswith("help"):
            keyboard = help_pannel(_)
            await message.reply_text(
                text="""Hola!!🧸
𝖨 𝖺𝗆 Mɪᴛᴀ, 𝗒𝗈𝗎𝗋 𝗉𝗈𝗐𝖾𝗋𝗋𝗎𝗅 & 𝗆𝗂𝗌𝗂𝗗𝗂𝗍𝗁𝗇𝗂𝗇𝗀 𝗆𝖺𝗇𝖺𝗀𝖾𝗆𝖾𝗇𝗍 𝖻𝗈𝗍, 𝖽𝖾𝗌𝗂𝗀𝗇𝖾𝖽 𝗍𝗈 𝗁𝖾𝗅𝗉 𝗒𝗈𝗎 𝗍𝗈𝗍𝖺ʟ 𝗈𝗏𝖾𝗋 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉𝗌 𝖾𝖺𝗌𝗂𝗅𝗒 𝗎𝗌𝗂𝗇𝗀 𝗆𝗒 𝗉𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝗆𝗈𝖽𝗎𝗅𝖾𝗌 𝖺𝗇𝖽 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌!

✨ 𝖶𝗁𝖺𝗍 𝖨 𝖢𝖺𝗇 𝖣𝗈:
 • 𝖲𝖾𝖺𝗆𝗅𝖾𝗌𝗌 𝗆𝖺𝗇𝖺𝗀𝖾𝗆𝖾𝗇𝗍 𝗈𝖿 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉𝗌
 • 𝖯𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝗆𝗈𝖽𝖾𝗋𝖺𝗍𝗂𝗈𝗇 𝗍𝗈𝗈𝗅𝗌
 • 𝖥𝗎𝗇 𝖺𝗇𝖽 𝖾𝗇𝗀𝖺𝗀𝗂𝗇𝗀 𝖿𝖾𝖺𝗍𝗎𝗋ᴇ𝗌

📚 𝖭𝖾𝖾𝖽 𝖧𝖾𝗅𝗉?
𝖢𝗅𝗂𝖼𝗄 𝗍𝗁𝖾 𝖧𝖾𝗅𝗉 𝖻𝗎𝗍𝗍𝗈𝗇 𝖻𝗲𝗹𝗼𝘄 𝘁𝗼 𝗀𝗲𝘁 𝗮𝗹𝗹 𝗱𝗲𝘁𝗮𝗶𝗹𝘀.
""",
                reply_markup=keyboard
            )
            await message.react("🍓", big=True)
            return

        if name.startswith("sud"):
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴄʜᴇᴄᴋᴇᴅ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n"
                         f"<b>ᴜsᴇʀ ɪᴅ:</b> <code>{message.from_user.id}</code>\n"
                         f"<b>ᴜsᴇʀɴᴀᴍᴇ:</b> @{message.from_user.username}",
                )
            return

        if name.startswith("inf"):
            m = await message.reply_text("💞")
            query = name.replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            next_result = await results.next()

            if isinstance(next_result, dict) and "result" in next_result:
                for result in next_result["result"]:
                    title = result["title"]
                    duration = result["duration"]
                    views = result["viewCount"]["short"]
                    thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                    channellink = result["channel"]["link"]
                    channel = result["channel"]["name"]
                    link = result["link"]
                    published = result["publishedTime"]
                    searched_text = _["start_6"].format(
                        title, duration, views, published, channellink, channel
                    )
                    key = InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="ʏᴏᴜᴛᴜʙᴇ", url=link)]]
                    )
                await m.delete()

                await app.send_photo(
                    chat_id=message.chat.id,
                    photo=thumbnail,
                    caption=searched_text,
                    reply_markup=key,
                )
                if await is_on_off(2):
                    await app.send_message(
                        chat_id=config.LOGGER_ID,
                        text=f"<b>{message.from_user.mention} ᴄʜᴇᴄᴋᴇᴅ ᴛʀᴀᴄᴋ ɪɴғᴏ.</b>\n\n"
                             f"<b>• ɪᴅᴇɴᴛɪғɪᴇʀ ⌯</b> <code>{message.from_user.id}</code>\n"
                             f"<b>• ʜᴀɴᴅʟᴇ ⌯</b> {message.from_user.username}.t.me",
                    )
            else:
                await m.edit_text("ғᴀɪʟᴇᴅ ᴛᴏ ʀᴇᴛʀɪᴇᴠᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.")
            return

    # Normal Start (No Deep Link)
    out = private_panel(_)
    await message.reply_text(
       text="""Hola!!🧸
𝖨 𝖺𝗆 Mɪᴛᴀ, 𝗒𝗈𝗎𝗋 𝗉𝗈𝗐𝖾𝗋𝗋𝗎𝗅 & 𝗆𝗂𝗌𝗂𝗗𝗂𝗍𝗁𝗇𝗂𝗇𝗀 𝗆𝖺𝗇𝖺𝗀𝖾𝗆𝖾𝗇𝗍 𝖻𝗈𝗍, 𝖽𝖾𝗌𝗂𝗀𝗇𝖾𝖽 𝗍𝗈 𝗁𝖾𝗅𝗉 𝗒𝗈𝗎 𝗍𝗈𝗍𝖺ʟ 𝗈𝗏𝖾𝗋 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉𝗌 𝖾𝖺𝗌𝗂𝗅𝗒 𝗎𝗌𝗂𝗇𝗀 𝗆𝗒 𝗉𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝗆𝗈𝖽𝗎𝗅𝖾𝗌 𝖺𝗇𝖽 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌!

✨ 𝖶𝗁𝖺𝗍 𝖨 𝖢𝖺𝗇 𝖣𝗈:
 • 𝖲𝖾𝖺𝗆𝗅𝖾𝗌𝗌 𝗆𝖺𝗇𝖺𝗀𝖾𝗆𝖾𝗇𝗍 𝗈𝖿 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉𝗌
 • 𝖯𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝗆𝗈𝖽𝖾𝗋𝖺𝗍𝗂𝗈𝗇 𝗍𝗈𝗈𝗅𝗌
 • 𝖥𝗎𝗇 𝖺𝗇𝖽 𝖾𝗇𝗀𝖺𝗀𝗂𝗇𝗀 𝖿𝖾𝖺𝗍𝗎𝗋ᴇ𝗌

📚 𝖭𝖾𝖾𝖽 𝖧𝖾𝗅𝗉?
𝖢𝗅𝗂𝖼𝗄 𝗍𝗁𝖾 𝖧𝖾𝗅𝗉 𝖻𝗎𝗍𝗍𝗈𝗇 𝖻𝗲𝗹𝗼𝘄 𝘁𝗼 𝗀𝗲𝘁 𝗮𝗹𝗹 𝗱𝗲𝘁𝗮𝗶𝗹𝘀.
""",
        reply_markup=InlineKeyboardMarkup(out),
    )
    if await is_on_off(2):
        await app.send_message(
            chat_id=config.LOGGER_ID,
            text=f"<b>{message.from_user.mention} sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.</b>\n\n"
                 f"<b>• ɪᴅᴇɴᴛɪғɪᴇʀ :</b> <code>{message.from_user.id}</code>\n"
                 f"<b>• ʜᴀɴᴅʟᴇ :</b> {message.from_user.username}.t.me",
        )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_text(
        text=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_text(
                    _["start_3"].format(
                        message.from_user.first_name,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
