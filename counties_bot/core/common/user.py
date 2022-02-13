from storage import interface as interface_storage


async def is_user_exist(user_id: int) -> bool:
    return await interface_storage.is_user_exist(
        user_id=user_id
    )


async def create_user(user_id: int):
    await interface_storage.create_user(
        user_id=user_id
    )
