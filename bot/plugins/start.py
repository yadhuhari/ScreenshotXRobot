from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot
import random

PICS = [
  "https://telegra.ph/file/4198a7f021bab17dea851.mp4"
]

@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m):

    await m.reply_video(
        video=random.choice(PICS)
        caption=f"""Hey there {m.from_user.mention} 👋,

I am an Advanced Screenshot X Bot, I can provide the screenshots & sample video of your files..😍

Just Send me a file and see the magic..✨""",
        quote=True,
        reply_markup=InlineKeyboardMarkup( [[
        InlineKeyboardButton("Source Code ✨", url="https://github.com/odysseusmax/animated-lamp")
        ]]
        )
    )
