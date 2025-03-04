from pyrogram import Client 
from pyrogram import __version__
from bot import Bot
from config import *
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import add_user, del_user, full_userbase, present_user

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=("<b>» ᴏᴡɴᴇʀ: <a href=http://t.me/Kakashi_The_Star>𝚜ᴏʙᴜᴢ</a>\n» 𝙵ᴏᴜɴᴅᴇʀ : <a href=http://t.me/Shimla_ki_Mirch>xᴀ-ʟɪɴ</a>\n» ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href=https://t.me/backupanimepoint>ᴠᴏʀᴛᴇ𝚡 𝙽ᴇᴛᴡᴏʀᴋ</a>\n» ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/+oM4CJ2tdJ3o3Y2Jl>ᴀɴɪᴍᴇ ᴠᴏʀᴛᴇ𝚡 </a>\n» ᴏɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/RyumaOngoingAnime>ᴏɴɢᴏɪɴɢ ᴠᴏʀᴛᴇ𝚡 </a>\n» ᴠᴏʀᴛᴇ𝚡 𝙽ᴇᴡ𝚜 : <a href=https://t.me/+In6rvaacWcA4NDc1>ᴠᴏʀᴛᴇ𝚡 𝙽ᴇᴡ𝚜</a>\n» ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/i_killed_my_clan>ᴏʙɪᴛᴏ</a></b>"),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('• ʜᴏᴍᴇ', callback_data='start'),
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ •", callback_data='close')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    
