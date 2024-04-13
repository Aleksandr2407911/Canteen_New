from aiogram.types import Message
from config import config_my

def is_admin_filter(message: Message) -> bool:
    return message.from_user.id in config_my.tg_bot.admin_ids
