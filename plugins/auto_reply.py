import asyncio, re
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from vars import FROM_GRP

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

lock = asyncio.Lock()

@Client.on_message(filters.chat(FROM_GRP))
async def auto_reply(bot, message):
    async with lock:
        try:
            await message.reply_text('''Meri Profile Pr Jaao Wahan Movie Search Group Hai Wahan Movie Search Kro Free me No Ads Join And Enjoy..

@Arpitbotmovies
@Arpitbotmovies''', reply_to_message_id=message.id)
            await asyncio.sleep(2)
        except FloodWait as e:
            logger.warning(f"Got FloodWait.\n\nWaiting for {e.value} seconds.")
            await asyncio.sleep(e.value + 2)
            logger.info("Floodwait ended")
            