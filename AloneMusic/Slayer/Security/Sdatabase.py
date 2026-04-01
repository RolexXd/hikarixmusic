import re

from bot.config import DB_NAME, MONGO_URI
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

# Collections
groups = db.groups
abuse_words = db.abuse_words
gban_users = db.gban_users
gmute_users = db.gmute_users

# =====================================================
# 🔹 GROUP SYSTEM
# =====================================================


async def add_group(group_id):
    if not await groups.find_one({"_id": group_id}):
        await groups.insert_one({"_id": group_id, "delay": 5})


async def get_delay(group_id):
    data = await groups.find_one({"_id": group_id})
    return data.get("delay", 5) if data else 5


async def set_delay(group_id, delay):
    await groups.update_one({"_id": group_id}, {"$set": {"delay": delay}}, upsert=True)


# =====================================================
# 🔹 ABUSE WORD SYSTEM
# =====================================================


async def add_abuse_word(word):
    word = word.lower().strip()
    if not await abuse_words.find_one({"word": word}):
        await abuse_words.insert_one({"word": word})


async def remove_abuse_word(word):
    word = word.lower().strip()
    await abuse_words.delete_one({"word": word})


async def get_abuse_words():
    return [x["word"] async for x in abuse_words.find()]


async def is_abuse(text):
    if not text:
        return False

    words = await get_abuse_words()
    if not words:
        return False

    pattern = r"\b(" + "|".join(map(re.escape, words)) + r")\b"
    return re.search(pattern, text.lower()) is not None


# =====================================================
# 🔹 GLOBAL BAN SYSTEM
# =====================================================


async def gban_user(user_id):
    if not await gban_users.find_one({"_id": user_id}):
        await gban_users.insert_one({"_id": user_id})


async def ungban_user(user_id):
    await gban_users.delete_one({"_id": user_id})


async def is_gbanned(user_id):
    return await gban_users.find_one({"_id": user_id}) is not None


# =====================================================
# 🔹 GLOBAL MUTE SYSTEM
# =====================================================


async def gmute_user(user_id):
    if not await gmute_users.find_one({"_id": user_id}):
        await gmute_users.insert_one({"_id": user_id})


async def ungmute_user(user_id):
    await gmute_users.delete_one({"_id": user_id})


async def is_gmuted(user_id):
    return await gmute_users.find_one({"_id": user_id}) is not None


# =====================================================
# 🔹 DEFAULT DATA LOADER
# =====================================================


async def load_default_data():
    default_words = [
        "idiot",
        "stupid",
        "noob",
        "fuck",
        "bitch",
        "asshole",
        "maderchod",
        "bahenchod",
        "mc",
        "mdc",
        "jhatu",
        "randi",
        "bkl",
        "lavda",
    ]

    for word in default_words:
        if not await abuse_words.find_one({"word": word}):
            await abuse_words.insert_one({"word": word})
