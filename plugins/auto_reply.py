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
            reply = await message.reply_text('''𝐈𝐌𝐏𝐎𝐑𝐓𝐀𝐍𝐓 𝐍𝐎𝐓𝐈𝐂𝐄 

𝗧𝗵𝗶𝘀 𝗚𝗿𝗼𝘂𝗽 𝗜𝘀 𝗗𝗲𝗮𝗱 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗼𝘃𝗶𝗲𝘀 𝗚𝗿𝗼𝘂𝗽 👇👇

𝗔𝗹𝗹 𝗧𝘆𝗽𝗲𝘀 𝗢𝗳 𝗠𝗼𝘃𝗶𝗲𝘀 𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲

 @FilmCityMoviesRequest   
 @FilmCityMoviesRequest    
 @FilmCityMoviesRequest


''', reply_to_message_id=message.id)

            await asyncio.sleep(2)
        except FloodWait as e:
            logger.warning(f"Got FloodWait.\n\nWaiting for {e.value} seconds.")
            await asyncio.sleep(e.value + 2)
            logger.info("Floodwait ended")

    try:
        await asyncio.sleep(10800)
        await reply.delete()
    except:
        pass
            
