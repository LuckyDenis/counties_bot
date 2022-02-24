import logging

import asyncpg

from aiogram import executor

from config import reader as config_reader


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


async def polling_on_startup(bot_dispatcher):
    from common import staff
    from interface import i18n

    database_cfg = config_reader.get_database_config()
    pool = await asyncpg.create_pool(
        user=database_cfg.user,
        password=database_cfg.password,
        host=database_cfg.host,
        port=database_cfg.port,
        database=database_cfg.dbname,
    )

    i18n_cfg = config_reader.get_i18n_config()
    i18n = i18n.I18N(
        domain=i18n_cfg.domain,
        default=i18n_cfg.default,
    )

    user_cfg = config_reader.get_user_config()

    dependence = staff.Dependence(
        pool=pool,
        i18n=i18n,
        user=user_cfg,
    )

    setattr(bot_dispatcher, 'dependence', dependence)


async def polling_on_shutdown(bot_dispatcher):
    dependence = getattr(bot_dispatcher, 'dependence', None)
    if dependence and dependence.pool:
        await dependence.pool.close()


def main():
    from controller import endpoint

    bot_cfg = config_reader.get_bot_config()
    if bot_cfg.is_use_polling:
        executor.start_polling(
            dispatcher=endpoint.dp,
            on_startup=polling_on_startup,
            on_shutdown=polling_on_shutdown,
            skip_updates=bot_cfg.skip_updates,
            timeout=bot_cfg.timeout,
            fast=bot_cfg.fast,
            relax=bot_cfg.relax,
        )
    else:
        pass  # todo: for webhook


if __name__ == '__main__':
    main()
