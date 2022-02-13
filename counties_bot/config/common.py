import os
import pathlib

import yaml


def _get_env_value(env_name: str) -> str:
    return os.getenv(env_name)


def _get_config_path(env_name: str) -> pathlib.Path:
    env_value = _get_env_value(env_name)
    if not env_value:
        raise RuntimeError(f'Ошибка запуска. Значение {env_value} не найдено')

    path = pathlib.Path(env_value)
    if not path.exists():
        raise RuntimeError(f'Ошибка чтения. Конфиг {path} не найден')

    if not path.is_file():
        raise RuntimeError(f'Ошибка чтения. Конфиг {path} директория')

    return path


def read_config(env_name: str) -> dict:
    config_path = _get_config_path(env_name)
    with open(config_path) as stream:
        return yaml.safe_load(stream)
