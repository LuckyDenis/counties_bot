import typing

import aiogram

from interface import common as icommon


async def send_messages(
        bot: aiogram.Bot, answers: typing.List[icommon.BaseMessage]
):
    for message in answers:
        if message.msg_type == icommon.MessageType.TEXT:
            message: icommon.TextMessage
            await _send_msg_with_text(bot, message)


async def _send_msg_with_text(
        bot: aiogram.Bot, message: icommon.TextMessage):
    await bot.send_message(
        chat_id=message.chat_id,
        text=message.text,
    )
