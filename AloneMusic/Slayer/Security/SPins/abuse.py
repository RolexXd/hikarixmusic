from pyrogram import Client, filters

from AloneMusic.Slayer.Security.Sdatabase import abuse_words


@Client.on_message(filters.group & filters.text)
async def abuse_filter(client, message):
    async for w in abuse_words.find():
        if w["word"] in message.text.lower():
            await message.delete()
            await message.reply("🚫 Abusive message removed")
            return
