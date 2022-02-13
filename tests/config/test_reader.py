import pytest

from counties_bot.config import reader


@pytest.mark.parametrize(
    ('config_func', 'attrs'),
    (
            (
                    reader.get_database_config,
                    ('user', 'password', 'host', 'port', 'dbname')
            ),
            (
                    reader.get_bot_config,
                    ('host', 'port', 'token', 'is_use_polling')
            ),
            (
                    reader.get_webhook_config,
                    ('host', 'path')
            ),
    )
)
def test_open_config(config_func, attrs):
    obj_cfg = config_func()
    for attr in attrs:
        assert getattr(obj_cfg, attr)
