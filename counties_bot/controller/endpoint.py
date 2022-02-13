import typing

from aiogram import Bot, Dispatcher, types

from core import runner as core_runner
from config import reader as config_reader
from interface import command as ui_cmd
from interface import common as ui_common


from controller import sender as bot_sender


bot_cfg = config_reader.get_bot_config()

bot = Bot(token=bot_cfg.token)
dp = Dispatcher(bot)


@dp.message_handler(commands=[ui_cmd.Start.as_text()])
async def start(message: types.Message):
    user_id = message.chat.id
    message_id = message.message_id
    track_code = f'tk-{user_id}-{message_id}'
    language = message.from_user.language_code or 'en'
    pool = getattr(dp, 'pool')

    start_state = core_runner.Start(
        user_id=user_id,
        language=language,
        track_code=track_code,
        pool=pool
    )
    await start_state.run()
    answers: typing.List[ui_common.BaseMessage] = (
        start_state.get_answers()
    )

    await bot_sender.send_messages(bot, answers)
