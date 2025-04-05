import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "23023763"))
API_HASH = getenv("API_HASH", "2f8b093168766704796f1acf6a9830b1")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","7812885136:AAHx37VLHWULgzfQZa_82TDSV6o6XsPc3Wk")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://musicbotxd:musicbotxd@cluster0.6thyk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002451411810))

# Get this value from @purvi_music_bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7348989193))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Abhimusicss/ABHIOP90",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PlusBotsMusic")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/plussupportchat")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @king_string_session_bot on Telegram
STRING1 = getenv("STRING_SESSION","BQFfUJMAZsuQwuc70zUrHK85g2cT6K3b2e5oU8BnI7SCgzCRdIdO84T7TJRfL7WjMAKyTJim5vI2-Gg_xhAKOD_zPuNOLB9du_k5gO_lhFr8wn1MfbT8NvDVXXa3NDyr0B_rrH_kxD0q26-shF1Sb6Nk9Ihg9eq-9sIMUnfFy6Elj7Uvod6nFXbR_Hq1mwDHJnMc3q7tMnUAvpAjH2iCKPTMktd5OTpMWN4esSHwYl451pwyHTy0XVQp3zbOEPcbJ3gXjMKnAC6xztLnXM0NEHGeSa4PxkGrlx8FKHlFgU1ymKdWUQA7AgVYTKL5WQhZUq4K1Gxg0aiKLU0n5INgV7KHCCvNQAAAAAHlIenxAA")
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
    "START_IMG_URL", "https://graph.org/file/9355a37178ac337a74f22-84e81139c63892bd73.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/7793dd6a86ad943366dd8-cd4fecd427fc7b0bd8.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/b6622cff41c5a66183caa-1c369e0581a4da6bbe.jpg"
STATS_IMG_URL = "https://graph.org/file/9d22f03239c64f922ee41-0c27b5e62b37153b48.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/b6622cff41c5a66183caa-1c369e0581a4da6bbe.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/b6622cff41c5a66183caa-1c369e0581a4da6bbe.jpg"
STREAM_IMG_URL = "https://graph.org/file/b6622cff41c5a66183caa-1c369e0581a4da6bbe.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/b6622cff41c5a66183caa-1c369e0581a4da6bbe.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/b6622cff41c5a66183caa-1c369e0581a4da6bbe.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/4cde3bd2af120694cf833-d42df60d016043b483.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/b6622cff41c5a66183caa-1c369e0581a4da6bbe.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/b6622cff41c5a66183caa-1c369e0581a4da6bbe.jpg"


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
