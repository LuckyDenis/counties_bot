import dataclasses
import typing

import asyncpg

from interface import i18n  # noqa: F401
from config import reader  # noqa: F401


@dataclasses.dataclass(frozen=True)
class Dependence:
    pool: typing.Optional[asyncpg.Pool]
    i18n: typing.Optional[i18n.I18N]  # noqa: F811
    user: typing.Optional[reader.UserConfig]  # noqa: F811
