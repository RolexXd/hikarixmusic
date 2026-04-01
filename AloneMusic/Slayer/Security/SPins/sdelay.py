from pyrogram import Client, filters

from AloneMusic.Slayer.Security.Sdatabase import groups


@Client.on_message(filters.command("setdelay") & filters.group)
async def setdelay(client, message):
    if len(message.command) != 2 or not message.command[1].isdigit():
        return
    delay = int(message.command[1])
    await groups.update_one(
        {"chat_id": message.chat.id}, {"$set": {"delay": delay}}, upsert=True
    )
    await message.reply(f"🕒 Auto delete set to {delay}s")
