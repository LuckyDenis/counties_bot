import typing

from aiogram import Bot, Dispatcher, types

from config import reader as config_reader
from controller import sender as bot_sender
from core import runner as core_runner
from interface import command as ui_cmd
from interface import common as ui_common
from controller import common

bot_cfg = config_reader.get_bot_config()

bot = Bot(token=bot_cfg.token)
dp = Dispatcher(bot)


@dp.message_handler(commands=[ui_cmd.Start.as_text()])
async def start(message: types.Message):
    pool = common.get_db_pool(dp)
    track_code = common.get_track_code(message)
    user_id = common.get_user_id(message)
    language = common.get_user_language(message)

    core_result = core_runner.Start(
        pool=pool,
        user_id=user_id,
        language=language,
        track_code=track_code,
    )
    await core_result.run()
    answers: typing.List[ui_common.BaseMessage] = (
        core_result.get_answers()
    )

    await bot_sender.send_messages(bot, answers)


@dp.message_handler(commands=[ui_cmd.Accept.as_text()])
async def accept(message: types.Message):
    pool = common.get_db_pool(dp)
    track_code = common.get_track_code(message)
    user_id = common.get_user_id(message)

    core_result = core_runner.Accept(
        pool=pool,
        user_id=user_id,
        track_code=track_code,
    )
    await core_result.run()
    answers: typing.List[ui_common.BaseMessage] = (
        core_result.get_answers()
    )

    await bot_sender.send_messages(bot, answers)
