from . import common
from . import consts


class BaseConfig:
    def __init__(self, config: dict):
        self._config: dict = config or {}

    def _get_variable(self, variable_name: str, default=None):
        return self._config.get(variable_name, default)


class DatabaseConfig(BaseConfig):
    @property
    def port(self) -> int:
        return self._get_variable('port', 5432)

    @property
    def host(self) -> str:
        return self._get_variable('host', '127.0.0.1')

    @property
    def dbname(self) -> str:
        return self._get_variable('dbname', 'tkm_db_dev')

    @property
    def user(self) -> str:
        return self._get_variable('user', 'postgres')

    @property
    def password(self) -> str:
        return self._get_variable('password', 'postgres')


class BotConfig(BaseConfig):
    @property
    def token(self) -> str:
        return self._get_variable('token', '')

    @property
    def host(self) -> str:
        return self._get_variable('host', '127.0.0.1')

    @property
    def port(self) -> int:
        return self._get_variable('port', '44300')

    @property
    def is_use_polling(self) -> bool:
        return self._get_variable('is_use_polling', True)

    @property
    def skip_updates(self):
        return self._get_variable('skip_updates', False)

    @property
    def timeout(self):
        return self._get_variable('timeout', 20)

    @property
    def relax(self):
        return self._get_variable('relax', 0.1)

    @property
    def fast(self):
        return self._get_variable('fast', True)


class WebHookConfig(BaseConfig):
    @property
    def path(self) -> int:
        return self._get_variable('port', '443')

    @property
    def host(self) -> str:
        return self._get_variable('host', '127.0.0.1')


class I18NConfig(BaseConfig):
    @property
    def domain(self) -> str:
        return self._get_variable('domain', 'counties_bot')

    @property
    def default(self) -> str:
        return self._get_variable('default', 'en')


class UserConfig(BaseConfig):
    @property
    def coin(self) -> int:
        return self._get_variable('coin', 0)

    @property
    def gem(self) -> int:
        return self._get_variable('gem', 0)

    @property
    def backpack(self) -> int:
        return self._get_variable('backpack', 1)


def get_database_config() -> DatabaseConfig:
    config = common.read_config(consts.COUNTIES_DB)
    return DatabaseConfig(config)


def get_bot_config() -> BotConfig:
    config = common.read_config(consts.COUNTIES_BOT)
    return BotConfig(config)


def get_webhook_config() -> WebHookConfig:
    config = common.read_config(consts.COUNTIES_WEBHOOK)
    return WebHookConfig(config)


def get_i18n_config() -> I18NConfig:
    config = common.read_config(consts.COUNTIES_I18N)
    return I18NConfig(config)


def get_user_config() -> UserConfig:
    config = common.read_config(consts.COUNTIES_USER)
    return UserConfig(config)
