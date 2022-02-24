import aiogram

from aiogram import types as aiogram_types

from common import staff as common_staff


def get_user_id(message: aiogram_types.Message) -> int:
    return message.chat.id


def get_track_code(message: aiogram_types.Message) -> str:
    user_id = message.chat.id
    message_id = message.message_id
    return f'tk-{user_id}-{message_id}'


def get_user_language(message: aiogram_types.Message) -> str:
    return message.from_user.language_code


def get_dependence(
        dp: aiogram.Dispatcher
) -> common_staff.Dependence:
    return getattr(dp, 'dependence')
