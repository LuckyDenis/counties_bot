from aiogram import Bot, Dispatcher, types

from config import reader as config_reader
from interface import command as icmd

bot_cfg = config_reader.get_bot_config()

bot = Bot(token=bot_cfg.token)
dp = Dispatcher(bot)


@dp.message_handler(commands=[icmd.Start.as_text()])
async def start(message: types.Message):
    await bot.send_message(
        message.chat.id,
        text=f'Эхо {message.text}'
    )
