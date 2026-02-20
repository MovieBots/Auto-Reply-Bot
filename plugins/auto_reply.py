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

AUTO_REPLY_TEXT = "ʸᴼᵁᴿ ᴹᴼⱽᴵᴱ ᴸᴵᴺᴷ ᴵᴺ ᴹʸ ᴾᴿᴼᶠᴵᴸᴱ ᴮᴵᴼ ᶜᴴᴱᶜᴷ ᴬᴺᴰ ˢᴱᴬᴿᶜᴴ"
last_message_id = {}

@Client.on_message(filters.group)
async def auto_reply(client, message):

    if not message.from_user:
        return

    me = await client.get_me()

    # Ignore yourself
    if message.from_user.id == me.id:
        return

    # Ignore bots
    if message.from_user.is_bot:
        return

    chat_id = message.chat.id

    # Only reply to latest message once
    if chat_id in last_message_id:
        if message.id <= last_message_id[chat_id]:
            return

    last_message_id[chat_id] = message.id

    try:
        reply = await message.reply_text(AUTO_REPLY_TEXT)

        await asyncio.sleep(20)
        await reply.delete()

    except Exception as e:
        print(e)

            
