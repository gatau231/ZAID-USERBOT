import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "24821011")) #optional
API_HASH = getenv("API_HASH", "bc0d32d5fc5d5137420284c2176600ed") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8024743123").split()))
OWNER_ID = int(getenv("8024743123"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "7987525124:AAEJyYgjyxkFJviDOig5LPrZqQaokoEWoTs")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("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") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "1BVtsOHYBu4DYbQ6OQo42ibR41BgxnDV2P-AsKhcNoTM14nor7Z2hz412EQAC0MvPZBPKQOrmkQzSJ-P0qjG5AkiJpn89dcbjelyT-jNQtcbwHkwaVDZ56iLr2PP4Bq_A67YhAkp6TRgAiMKjzAfmT7nya1WuSKYIN1WCX55p3zeE7kr1sPqXEdoZ9-tVisqbFk8Tb9OoPLUQ3-fbo9zJuHKT7XH2MLJy3BEBV7tCgcU5Guax2qCr-QxifzFuJNuo3l05jSSevabDC7urTm0hQXntSIcLNrKekA_OZK8C72j1XZ7fHoTBhIbhZiOnnqLWy8EybRspoPaoH0B3cI6v9GAKcvHRzoU=")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
