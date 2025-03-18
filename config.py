#The repo is fully coded and modified by @Dypixx.
#Please do not sell or remove credits.

import os

API_ID = os.getenv("API_ID", "29171167")
API_HASH = os.getenv("API_HASH", "7ea2149629e445936619f06a3c0dc716")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN = int(os.getenv("ADMIN", "7251898668"))

DUMP_CHANNEL = int(os.getenv("DUMP_CHANNEL", "-1002264638393")) #Channel Id
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002264638393"))

DB_URI = os.getenv("DB_URI", "mongodb+srv://tg:tg@cluster0.fekvk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.getenv("DB_NAME", "cluster0")

IS_FSUB = bool(os.environ.get("FSUB", True)) # Set "True" For Force Subscribe Enable
AUTH_CHANNELS = os.environ.get("AUTH_CHANNEL", "-1002442422204") # Add Multiple Channels iD By Space
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")] # DONT TOUCH

ENABLE_FLOOD_WAIT = bool(os.getenv("ENABLE_FLOOD_WAIT", False)) # Set "True" For Enable Floodwait
FLOOD_WAIT_TIME = int(os.getenv("FLOOD_WAIT_TIME", 300)) #5min
