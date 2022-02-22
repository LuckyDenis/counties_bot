import aiogram
import asyncpg
from aiogram import types as aiogram_types


def get_user_id(message: aiogram_types.Message) -> int:
    return message.chat.id


def get_track_code(message: aiogram_types.Message) -> str:
    user_id = message.chat.id
    message_id = message.message_id
    return f'tk-{user_id}-{message_id}'


def get_user_language(message: aiogram_types.Message) -> str:
    return message.from_user.language_code


def get_db_pool(dp: aiogram.Dispatcher) -> asyncpg.Pool:
    return getattr(dp, 'pool')
