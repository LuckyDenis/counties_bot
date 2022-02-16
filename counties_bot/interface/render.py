from interface import errors
from interface import common
from interface import command


class BaseRender:
    @classmethod
    async def render(
            cls, render_data: common.BaseRenderReq
    ) -> common.BaseMessage:
        try:
            return await cls._render(render_data)
        except errors.BaseRenderError:
            raise

    @classmethod
    async def _render(
            cls, render_data: common.BaseRenderReq
    ) -> common.BaseMessage:
        raise NotImplementedError()


class NewUser(BaseRender):
    @classmethod
    async def _render(
            cls, render_data: common.BaseRenderReq
    ) -> common.BaseMessage:
        return common.TextMessage(
            user_id=render_data.user_id,
            track_code=render_data.track_code,
            text='Новый пользователь ' + command.Start.as_cmd()
        )


class OldUserAccepted(BaseRender):
    @classmethod
    async def _render(
            cls, render_data: common.BaseRenderReq
    ) -> common.BaseMessage:
        return common.TextMessage(
            user_id=render_data.user_id,
            track_code=render_data.track_code,
            text='Старый пользователь согласился' + command.Start.as_cmd()
        )


class OldUserIsNotAccepted(BaseRender):
    @classmethod
    async def _render(
            cls, render_data: common.BaseRenderReq
    ) -> common.BaseMessage:
        return common.TextMessage(
            user_id=render_data.user_id,
            track_code=render_data.track_code,
            text='Старый пользователь не согласился' + command.Start.as_cmd()
        )
