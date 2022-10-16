import logging
from pyrogram import Client, filters
from database.ia_filterdb import Media
from info import ADMINS
logger = logging.getLogger(__name__)

@Client.on_message(filters.command('total') & filters.user(ADMINS))
async def total(bot, message):

    msg = await message.reply("Processing...⏳", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁 Saved files: {total}')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')
