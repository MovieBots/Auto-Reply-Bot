import asyncio, re
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from vars import FROM_GRP

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

lock = asyncio.Lock()

@Client.on_message(filters.chat(FROM_GRP) & ~filters.bot)
async def auto_reply(bot, message):
    async with lock:
        try:
            reply = await message.reply_text('''𝐘𝐎𝐔𝐑 𝐌𝐎𝐕𝐈𝐄 𝐋𝐈𝐍𝐊 𝐈𝐍 𝐌𝐘 𝐏𝐑𝐎𝐅𝐈𝐋𝐄 𝐁𝐈𝐎 𝐂𝐇𝐄𝐂𝐊 𝐀𝐍𝐃 𝐒𝐄𝐀𝐑𝐂𝐇


''', reply_to_message_id=message.id)

            await asyncio.sleep(2)
        except FloodWait as e:
            logger.warning(f"Got FloodWait.\n\nWaiting for {e.value} seconds.")
            await asyncio.sleep(e.value + 2)
            logger.info("Floodwait ended")

    try:
        await asyncio.sleep(3600)
        await reply.delete()
    except:
        pass
            
