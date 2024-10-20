from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 28436511))
API_HASH = getenv("API_HASH", "0114c36706aca2c07acc12046c15e3f6")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", 6260080241))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "ANJALIWORLD")
UPDATE_CHNL = getenv("UPDATE_CHNL", "ANJALINETWORK")
OWNER_USERNAME = getenv("OWNER_USERNAME", "AnjaliOwnerBot")

# Random Start Images
IMG = [
    "https://envs.sh/qii.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgQAAxkBAALRi2NZXUgjZCT775L5Nr0XrLbQ6XIpAAK_EQACpvFxHq2xh5JRVJNrKgQ",
    "CAACAgQAAxkBAALRjGNZXUs6YPggISBdtg4nXaU0vjNzAALqCwACbCIRU61ZQKi3F88DKgQ",
    "CAACAgQAAxkBAALRjWNZXUvETcfHR2Yi9ftTQLLP2uD8AAIVDAAC1SMQU-QrCHEcbz8rKgQ",
]


EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]
