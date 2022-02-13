async def is_user_exist(user_id: int) -> bool:
    return False


async def create_user(user_id: int):
    return {
        'user_id': user_id
    }
