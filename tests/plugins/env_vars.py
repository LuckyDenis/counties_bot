import os
import pathlib

import pytest

from counties_bot.config import consts as config_consts


test_root_dir = pathlib.Path(__file__)
project_root = test_root_dir.parent.parent.parent
etc_dir = project_root.joinpath('etc')
project_config_dir = etc_dir.joinpath('counties')


@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests(*_):
    os.environ[config_consts.COUNTIES_BOT] = (
        str(project_config_dir.joinpath(config_consts.COUNTIES_BOT + '.yaml'))
    )

    os.environ[config_consts.COUNTIES_DB] = (
        str(project_config_dir.joinpath(config_consts.COUNTIES_DB + '.yaml'))
    )

    os.environ[config_consts.COUNTIES_WEBHOOK] = (
        str(project_config_dir.joinpath(config_consts.COUNTIES_WEBHOOK + '.yaml'))
    )
