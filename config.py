from os import environ as env

class Config:
    API_ID = int(env.get("API_ID", "21134445")) #TG API ID
    API_HASH = env.get("API_HASH", "231c18ea7273824491d6bf05425ab74e
") #TG API HASH
    BOT_TOKEN = env.get("BOT_TOKEN", "7517513084:AAHMla-mLgYS11aeGXmk8c_4EWZYvNYk6TM") #Add Bot Token, get from botfather
    FSUB_ID = int(env.get("FSUB_ID", "-1002099263061"))  #Add Your FSub Channel Id -100xxxxxxxxx
    FSUB = bool(env.get("FSUB", True)) #Keep True If U Want Force Subscribe         
    SB_PIC = env.get("SST_PIC", "https://i.ibb.co/c6vkVBP/photo-2024-11-15-12-13-41-7437478159336865812.jpg") #Add Link For Start Cmd Pic
    BOT_USERNAME = env.get("BOT_USERNAME", "SST_REACTIONBOT") #Add Bot Username Without @
    EMOJIS = [
        "👍", "👎", "❤", "🔥", 
        "🥰", "👏", "😁", "🤔",
        "🤯", "😱", "🤬", "😢",
        "🥶", "🤩", "🤮", "💩",
        "🙏", "👌", "🤣", "🤡",
        "🥱", "🥴", "😍", "🤓",
        "❤‍🔥", "🌚", "😐", "💯",
        "🤣", "⚡", "🍌", "🏆",
        "💔", "🤨", "😐", "😡",
        "👅", "🆒", "🖕", "😈",
        "😴", "😭", "👻", "⚡",
        "👨‍💻", "👀", "🎃", "🙄",
        "😇", "😨", "🤝", "🤐",
        "🤗", "🫡", "🎅", "🥸",
        "🤫", "😶‍🌫", "🤪", "😏",
        "😘", "👾", "🤷‍♂", "😎"
    ]
