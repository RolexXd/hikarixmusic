#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
#
# This file is part of < https://github.com/TheAloneTeam/TheAloneMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/TheAloneMusic/blob/master/LICENSE >
# All rights reserved.

import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("22657083", 0))
API_HASH = getenv("d6186691704bd901bdab275ceaab88f3")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("8752427731:AAFWD6FLAVe8YIGtjuTPZNEaEgRMufUnoWY")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://maxx99596_db_user:zXx9k0yY9ruCvNJV@cluster0.aamlvxf.mongodb.net/?appName=Cluster0", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

# Set this to true if you want post ads automatically
ADS_MODE = getenv("ADS_MODE", None)

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1003824737197", 0))

DEBUG_IGNORE_LOG = True
# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("5303251380", 5303251380))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("hikari")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HRKU-AArEwk2VzkV34TPhdvIMNUvVNUqOORRE2rKwVwZC0nqw_____wa5cyLZDJm9")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/RolexXd/hikarixmusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/OnyxCoders")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/LavenderEchoo")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", None))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://files.catbox.moe/34xlvu.jpg",
)
PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://files.catbox.moe/34xlvu.jpg",
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/d6d42f.jpg"
STATS_IMG_URL = "https://files.catbox.moe/d6d42f.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/d6d42f.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/d6d42f.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/d6d42f.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
