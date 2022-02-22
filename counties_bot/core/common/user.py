import asyncpg

from storage import query as storage_query


async def is_user_exist(pool: asyncpg.Pool, user_id: int) -> bool:
    return await storage_query.is_user_exist(
        pool=pool,
        user_id=user_id
    )


async def create_user(pool: asyncpg.Pool, user_id: int, language):
    await storage_query.create_user(
        pool=pool,
        user_id=user_id,
        language=language
    )


async def is_user_accept(pool: asyncpg.Pool, user_id: int) -> bool:
    return await storage_query.is_user_accept(
        pool=pool, user_id=user_id,
    )


async def get_user_language(pool: asyncpg.Pool, user_id: int) -> str:
    return await storage_query.get_user_language(
        pool=pool, user_id=user_id
    )


async def update_user_is_accept(pool: asyncpg.Pool, user_id: int) -> str:
    return await storage_query.update_user_is_accept(
        pool=pool, user_id=user_id
    )
