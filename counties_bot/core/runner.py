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
        CREATED_USER = enum.auto()
        DONE = enum.auto()
        IS_OLD_USER_ACCEPTED = enum.auto()
        OLD_USER_ACCEPTED = enum.auto()
        OLD_USER_IS_NOT_ACCEPTED = enum.auto()
        ADD_OLD_USER_LANGUAGE = enum.auto()

    def __init__(self, pool, user_id, language, track_code):
        self.state = self.State.START
        self.user_id = user_id
        self.language = language
        self.pool = pool
        self.answers = []
        self.track_code = track_code

    async def run(self):
        """
        START -- NEW_USER -- CREATED_USER --------
          |                                      |
        OLD_USER           OLD_USER_ACCEPTED -- DONE
         |                       |               |
        ADD_OLD_USER_LANGUAGE    |               |
         |                       |               |
        IS_OLD_USER_ACCEPTED -------- OLD_USER_IS_NOT_ACCEPTED
        """
        while self.state != self.State.DONE:
            if self.state == self.State.START:
                await self._start()
            if self.state == self.State.NEW_USER:
                await self._new_user()
            if self.state == self.State.CREATED_USER:
                await self._create_user()
            if self.state == self.State.OLD_USER:
                await self._add_old_user_language()
            if self.state == self.State.ADD_OLD_USER_LANGUAGE:
                await self._is_old_user_accepted()
            if self.state == self.State.OLD_USER_ACCEPTED:
                await self._old_user_accepted()
            if self.state == self.State.OLD_USER_IS_NOT_ACCEPTED:
                await self._old_user_is_not_accepted()

    def get_answers(self) -> typing.List[ui_common.BaseMessage]:
        return self.answers

    async def _start(self):
        is_user_exist = await user.is_user_exist(
            pool=self.pool,
            user_id=self.user_id
        )
        if not is_user_exist:
            self.state = self.State.NEW_USER
        else:
            self.state = self.State.OLD_USER

    async def _new_user(self):
        await user.create_user(self.pool, self.user_id, self.language)
        self.state = self.State.CREATED_USER

    async def _create_user(self):
        answer = await ui_render.NewUser.render(
            ui_common.NewUserReq(
                user_id=self.user_id,
                track_code=self.track_code,
                language=self.language,
            )
        )
        self.answers.append(answer)
        self.state = self.State.DONE

    async def _is_old_user_accepted(self):
        is_accepted = await user.is_user_accept(
            pool=self.pool,
            user_id=self.user_id,
        )
        if is_accepted:
            self.state = self.State.OLD_USER_ACCEPTED
        else:
            self.state = self.State.OLD_USER_IS_NOT_ACCEPTED

    async def _old_user_accepted(self):
        answer = await ui_render.OldUserAccepted.render(
            ui_common.OldUserAcceptedReq(
                user_id=self.user_id,
                language=self.language,
                track_code=self.track_code,
            )
        )
        self.answers.append(answer)
        self.state = self.State.DONE

    async def _old_user_is_not_accepted(self):
        answer = await ui_render.OldUserIsNotAccepted.render(
            ui_common.OldUserIsNotAcceptedReq(
                user_id=self.user_id,
                language=self.language,
                track_code=self.track_code,
            )
        )
        self.answers.append(answer)
        self.state = self.State.DONE

    async def _add_old_user_language(self):
        old_user_language = await user.get_user_language(
            pool=self.pool,
            user_id=self.user_id,
        )
        self.language = old_user_language
        self.state = self.State.ADD_OLD_USER_LANGUAGE


class Accept:
    class State(enum.Enum):
        START = enum.auto()
        DONE = enum.auto()
        ADD_USER_LANGUAGE = enum.auto()
        USER_IS_NOT_EXIST = enum.auto()
        UPDATE_USER_ACCEPT = enum.auto()

    def __init__(self, pool, user_id, track_code):
        self.state = self.State.START
        self.user_id = user_id
        self.language = 'en'
        self.pool = pool
        self.track_code = track_code
        self.answers = []

    async def run(self):
        """
        START -- USER_IS_NOT_EXIST -- DONE
         |                             |
        ADD_USER_LANGUAGE -- UPDATE_USER_ACCEPT
        """
        while self.state != self.State.DONE:
            if self.state == self.State.START:
                await self._start()
            if self.state == self.State.USER_IS_NOT_EXIST:
                await self._user_is_not_exist()
            if self.state == self.State.ADD_USER_LANGUAGE:
                await self._add_user_language()
            if self.state == self.State.UPDATE_USER_ACCEPT:
                await self._update_user_accept()

    async def get_answers(self) -> typing.List[ui_common.BaseMessage]:
        return self.answers

    async def _start(self):
        is_user_exist = await user.is_user_exist(
            pool=self.pool,
            user_id=self.user_id
        )
        if not is_user_exist:
            self.state = self.State.USER_IS_NOT_EXIST
        else:
            self.state = self.State.ADD_USER_LANGUAGE

    async def _add_user_language(self):
        old_user_language = await user.get_user_language(
            pool=self.pool,
            user_id=self.user_id,
        )
        self.language = old_user_language
        self.state = self.State.UPDATE_USER_ACCEPT

    async def _update_user_accept(self):
        self.state = self.State.DONE

    async def _user_is_not_exist(self):
        self.state = self.State.DONE
