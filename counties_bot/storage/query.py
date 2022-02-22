import asyncpg

from storage import template


async def is_user_exist(pool: asyncpg.Pool, user_id: int) -> bool:
    async with pool.acquire() as conn:
        conn: asyncpg.Connection
        res = await conn.fetchrow(template.IS_USER_EXIST, user_id)
    return res[0]


async def create_user(pool: asyncpg.Pool, user_id: int, language):
    async with pool.acquire() as conn:
        conn: asyncpg.Connection
        await conn.fetch(
            template.CREATE_NEW_USER,
            user_id, language,
        )


async def is_user_accept(pool: asyncpg.Pool, user_id: int) -> bool:
    async with pool.acquire() as conn:
        conn: asyncpg.Connection
        res = await conn.fetchrow(template.IS_USER_ACCEPT, user_id)
    return res[0]


async def get_user_language(pool: asyncpg.Pool, user_id: int) -> str:
    async with pool.acquire() as conn:
        conn: asyncpg.Connection
        res = await conn.fetchrow(template.GET_USER_LANGUAGE, user_id)
    return res['language']


async def update_user_is_accept(pool: asyncpg.Pool, user_id: int):
    async with pool.acquire() as conn:
        conn: asyncpg.Connection
        await conn.fetch(
            template.UPDATE_USER_ACCEPT,
            user_id, True,
        )
