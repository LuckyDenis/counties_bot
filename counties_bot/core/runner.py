import enum
import typing

from interface import render as ui_render
from interface import common as ui_common

from core.common import user


class Start:
    class State(enum.Enum):
        START = enum.auto()
        NEW_USER = enum.auto()
        OLD_USER = enum.auto()
        IS_USER_EXIST = enum.auto()
        CREATED_USER = enum.auto()
        DONE = enum.auto()

    def __init__(self, user_id, language, track_code, pool):
        self.state = self.State.START
        self.user_id = user_id
        self.language = language
        self.pool = pool
        self.answers = []
        self.track_code = track_code

    async def _start(self):
        is_user_exist = await user.is_user_exist(self.user_id)
        if not is_user_exist:
            self.state = self.State.NEW_USER
        else:
            self.state = self.State.OLD_USER

    async def _new_user(self):
        await user.create_user(self.user_id)
        self.state = self.State.CREATED_USER

    async def _create_user(self):
        answer = await ui_render.NewUser.render(
            ui_common.NewUserReq(
                chat_id=self.user_id,
                track_code=self.track_code,
                language=self.language,
            )
        )
        self.answers.append(answer)
        self.state = self.State.DONE

    async def _old_user(self):
        answer = await ui_render.OldUser.render(
            ui_common.NewUserReq(
                chat_id=self.user_id,
                track_code=self.track_code,
                language=self.language,
            )
        )
        self.answers.append(answer)
        self.state = self.State.DONE

    async def run(self):
        """
        START -- NEW_USER -- CREATED_USER
          |                       |
        OLD_USER -------------- DONE
        """
        if self.state == self.State.START:
            await self._start()
        if self.state == self.State.NEW_USER:
            await self._new_user()
        if self.state == self.State.CREATED_USER:
            await self._create_user()
        if self.state == self.State.OLD_USER:
            await self._old_user()

    def get_answers(self) -> typing.List[ui_common.BaseMessage]:
        return self.answers
