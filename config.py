#(©)t.me/CodeFlix_Bots




import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7869528679:AAG6b737YPh_Rk4DLQga4mC9DezrdDq8QpI")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "25839862"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ef417c527eae44d9ddb662743fbbedcc")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002354334037"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5585016974"))

#Port
PORT = os.environ.get("PORT", "8059")

DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://probito140:umaid2008@cluster0.1utfc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002436208049"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002198679064"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCESUB_CHANNEL3", "-1002180207210"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

HELP_TXT = "<b>ᴅᴍ <a href=https://t.me/i_killed_my_clan>ᴏʙɪᴛᴏ</a></b>"
ABOUT_TXT = "<b>» ᴏᴡɴᴇʀ: <a href=http://t.me/Kakashi_The_Star>𝚜ᴏʙᴜᴢ</a>\n» 𝙵ᴏᴜɴᴅᴇʀ : <a href=http://t.me/Shimla_ki_Mirch>xᴀ-ʟɪɴ</a>\n» ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href=https://t.me/backupanimepoint>ᴠᴏʀᴛᴇ𝚡 𝙽ᴇᴛᴡᴏʀᴋ</a>\n» ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/+oM4CJ2tdJ3o3Y2Jl>ᴀɴɪᴍᴇ ᴠᴏʀᴛᴇ𝚡 </a>\n» ᴏɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/RyumaOngoingAnime>ᴏɴɢᴏɪɴɢ ᴠᴏʀᴛᴇ𝚡 </a>\n» ᴠᴏʀᴛᴇ𝚡 𝙽ᴇᴡ𝚜 : <a href=https://t.me/+In6rvaacWcA4NDc1>ᴠᴏʀᴛᴇ𝚡 𝙽ᴇᴡ𝚜</a>\n» ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/i_killed_my_clan>ᴏʙɪᴛᴏ</a></b>"
START_PIC = os.environ.get("START_PIC", "https://envs.sh/7nm.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/7nm.jpg")

#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "30"))

START_MSG = os.environ.get("START_MESSAGE", "<b>ʙᴀᴋᴋᴀᴀᴀ!! {first}\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</b>")
try:
    ADMINS=[5585016974]
    for x in (os.environ.get("ADMINS", "7147032060 5726546571 5585016974").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(5585016974)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
