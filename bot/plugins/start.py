from pyrogram import filters as Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from ..translations import Messages as tr
from ..config import Config
from ..utubebot import UtubeBot


@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("start")
    & Filters.user(Config.AUTH_USERS)
)
async def _start(c: UtubeBot, m: Message):
    await m.reply_chat_action("typing")
    await m.reply_text(
        text=tr.START_MSG.format(m.from_user.first_name),
        quote=True,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
                  [
                      InlineKeyboardButton("☘️How To Use☘️", callback_data="/help")
                  ],
                  [
                      InlineKeyboardButton("🖥️Project Channel🇱🇰", url="https://t.me/Dasuking"),
                      InlineKeyboardButton("😌Support Owner✨", url="https://t.me/Dasuwaprofa")
                  ],
                  [  
                      InlineKeyboardButton("👻Another Projects🇱🇰", url="https://t.me/Dasuking")
                  ]]
        ),
    )
