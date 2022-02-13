import asyncpg

from aiogram import executor

from config import reader as config_reader


async def polling_on_startup(bot_dispatcher):
    database_cfg = config_reader.get_database_config()
    pool = await asyncpg.create_pool(
        user=database_cfg.user,
        password=database_cfg.password,
        host=database_cfg.host,
        port=database_cfg.port,
        database=database_cfg.dbname,
    )
    setattr(bot_dispatcher, 'pool', pool)


async def polling_on_shutdown(bot_dispatcher):
    pool: asyncpg.Pool = getattr(bot_dispatcher, 'pool')
    if pool:
        await pool.close()


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
