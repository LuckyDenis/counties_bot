import dataclasses


class BaseCommand:
    _cmd: str = 'base'
    _regexp: str = '*'

    @classmethod
    def as_text(cls, cell_id=None):
        return cls._cmd.format(cell_id=cell_id)

    @classmethod
    def as_cmd(cls, cell_id=None):
        return '/' + cls._cmd.format(cell_id=cell_id)

    @classmethod
    def as_regexp(cls):
        return cls._regexp


@dataclasses.dataclass(frozen=True)
class Start(BaseCommand):
    _cmd = 'start'


@dataclasses.dataclass(frozen=True)
class Help(BaseCommand):
    _cmd = 'help'


@dataclasses.dataclass(frozen=True)
class Accept(BaseCommand):
    _cmd = 'accept'
