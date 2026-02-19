import asyncio, re
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from vars import FROM_GRP

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

lock = asyncio.Lock()

import asyncio
from pyrogram import Client, filters

AUTO_REPLY_TEXT = "ʏօʊʀ ʍօʋɨɛ ɨռ ʍʏ քʀօʄɨʟɛ քʟɛǟֆɛ ƈɦɛƈӄ"

@Client.on_message(filters.group)
async def auto_reply(client, message):

    # Ignore service messages
    if not message.from_user:
        return

    me = await client.get_me()

    # Ignore yourself
    if message.from_user.id == me.id:
        return

    # Ignore bots (IMPORTANT FIX)
    if message.from_user.is_bot:
        return

    reply = await message.reply_text(AUTO_REPLY_TEXT)

    await asyncio.sleep(10)
    await reply.delete()


    except:
        pass
            
