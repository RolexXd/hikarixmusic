
import asyncio
from pyrogram import Client, filters
from AloneMusic.Slayer.Security.Sdatabase import groups

@Client.on_message(filters.group & filters.text)
async def auto_delete(client, message):
    data = await groups.find_one({"chat_id": message.chat.id})
    if not data or not data.get("delay"):
        return
    await asyncio.sleep(data["delay"])
    try:
        await message.delete()
    except:
        pass
